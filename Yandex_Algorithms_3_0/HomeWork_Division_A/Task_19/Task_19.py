# https://contest.yandex.ru/contest/45469/problems/19/
# Дивизион А
# 19. Коммерческий калькулятор
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = map(int, file.readline().split())
        numbers = list(map(int, file.readline().split()))
    return n, numbers


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


class HeapMin():
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
                if self.heap[parent_index] > self.heap[index_new_item]:
                    self.heap[parent_index], self.heap[index_new_item] = self.heap[index_new_item], self.heap[
                        parent_index]
                    index_new_item = parent_index
                else:
                    break

    def extract(self):
        size_heap = len(self.heap)
        extract_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        index_change_item = 0
        while index_change_item < size_heap - 2:
            index_children_left = (index_change_item + 1) * 2 - 1
            index_children_right = (index_change_item + 1) * 2

            if index_children_right > size_heap - 1 or index_children_left > size_heap - 1:
                break
            children_left = self.heap[index_children_left]
            children_right = self.heap[index_children_right]

            if children_right <= children_left and children_right <= self.heap[index_change_item]:
                self.heap[index_change_item], self.heap[index_children_right] = self.heap[index_children_right], \
                                                                                self.heap[index_change_item]
                index_change_item = index_children_right
            elif children_left < self.heap[index_change_item] and children_left <= children_right:
                self.heap[index_change_item], self.heap[index_children_left] = self.heap[index_children_left], \
                                                                               self.heap[index_change_item]
                index_change_item = index_children_left
            else:
                break
        # Удаляем последний элемент, который изначально скопировали вначало списка
        self.heap.pop()
        return extract_item


# Поиск минимальной цены за совершенные операции
def calc_price_operations(n, numbers):
    '''
    входные данные
    :n — кол-во операций
    :numbers — последовательность операндов

    выходные данные
    :sum_price - минимальная цена за совершенные операции
    '''
    heap = HeapMin()
    for num in numbers:
        heap.insert(num)

    sum_price = 0
    while len(heap.heap) > 1:
        num1 = heap.extract()
        num2 = heap.extract()
        num3 = num1 + num2
        heap.insert(num3)
        sum_price += num3 * 0.05
    return sum_price


def main():
    # считываем входные данные
    n, numbers = load_data(INPUT_FILE)
    # Поиск минимальной цены за совершенные операции
    min_price = calc_price_operations(n, numbers)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, f"{round(min_price, 2):.2f}")


if __name__ == "__main__":
    main()
