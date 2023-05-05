# https://contest.yandex.ru/contest/45469/problems/20/
# Дивизион А
# 20. Машинки
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, k, p = map(int, file.readline().split())
        cars = []
        for _ in range(p):
            cars.append(int(file.readline().strip()))
    return n, k, p, cars


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


class Heap():
    def __init__(self):
        self.heap = []

    def insert(self, n):
        if len(self.heap) == 0:
            self.heap.append(n)
        else:
            self.heap.append(n)
            index_new_item = len(self.heap) - 1
            while index_new_item > 0:
                parent_index = (index_new_item + 1) // 2 - 1
                if self.heap[parent_index][0] < self.heap[index_new_item][0]:
                    self.heap[parent_index], self.heap[index_new_item] = self.heap[index_new_item], self.heap[
                        parent_index]
                    index_new_item = parent_index
                else:
                    break

    def extract(self):
        extract_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        index_change_item = 0
        size_heap = len(self.heap)
        while index_change_item < len(self.heap) - 2:
            index_children_left = (index_change_item + 1) * 2 - 1
            index_children_right = (index_change_item + 1) * 2

            if index_children_right > size_heap - 1 or index_children_left > size_heap - 1:
                break
            children_left = self.heap[index_children_left]
            children_right = self.heap[index_children_right]

            if children_right[0] >= children_left[0] and children_right[0] > self.heap[index_change_item][0]:
                self.heap[index_change_item], self.heap[index_children_right] = self.heap[index_children_right], \
                                                                                self.heap[index_change_item]
                index_change_item = index_children_right
            elif children_left[0] > self.heap[index_change_item][0] and children_left[0] >= children_right[0]:
                self.heap[index_change_item], self.heap[index_children_left] = self.heap[index_children_left], \
                                                                               self.heap[index_change_item]
                index_change_item = index_children_left
            else:
                break
        # Удаляем последний элемент, который изначально скопировали вначало списка
        self.heap.pop()
        return extract_item


# Поиск минимума операций по выбору машинок
def calc_min_operations(n, k, p, cars):
    '''
    входные данные
    :n — кол-во различных машинок
    :k — кол-во машинок, которые могут находиться на полу
    :p - кол-во строк в списке машинок
    :numbers — последовательность операндов

    выходные данные
    :min_operations - минимум операций по выбору машинок
    '''

    min_operations = 0
    car_last_indexes = {}
    cars_positions = [math.inf] * p
    for i in range(p - 1, -1, -1):
        cars_positions[i] = car_last_indexes.get(cars[i], math.inf)
        car_last_indexes[cars[i]] = i

    heap_last_index = Heap()
    select_cars = set([])
    for index, car in enumerate(cars):
        if car not in select_cars:
            if len(select_cars) >= k:
                car_for_del = (-1, -1)
                while car_for_del[1] not in select_cars:
                    car_for_del = heap_last_index.extract()
                select_cars.remove(car_for_del[1])
            select_cars.add(car)
            heap_last_index.insert((cars_positions[index], car))
            min_operations += 1
        heap_last_index.insert((cars_positions[index], car))
    return min_operations


def main():
    # считываем входные данные
    n, k, p, cars = load_data(INPUT_FILE)
    # Поиск минимума операций по выбору машинок
    min_operations = calc_min_operations(n, k, p, cars)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_operations))


if __name__ == "__main__":
    main()
