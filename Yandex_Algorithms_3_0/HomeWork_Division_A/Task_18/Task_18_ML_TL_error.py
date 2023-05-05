# https://contest.yandex.ru/contest/45469/problems/18/
# Дивизион А
# 18. Тупики
import gc
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

TRAIN_IN = 1
TRAIN_OUT = 0


# Читаем данные из input.txt
def load_data(filename):
    trains = []
    with open(filename, "r") as file:
        k, n = list(map(int, file.readline().split()))
        for _ in range(n):
            time_in, time_out = tuple(map(int, file.readline().split()))
            trains.append((time_in, time_out))
    return k, trains


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


class HeapMin():
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def insert(self, n):
        if self.size() == 0:
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


# Расчет тупиков, куда придет поезд
def calc_stop_train(k, trains):
    '''
    входные данные
    :k — количество тупиков
    :trains (time_in, time_out) — время прибытия и отправления электрички

    выходные данные
    :result_stops_train - список гобилнов зашедших к шаману
    '''
    stops_heap = HeapMin()
    for i in range(k):
        stops_heap.insert(i + 1)
    events = []
    for number_train, (time_in, time_out) in enumerate(trains):
        events.append((time_in, number_train + 1, TRAIN_IN))
        events.append((time_out + 1, number_train + 1, TRAIN_OUT))
    events = sorted(events)
    gc.collect()
    stops_train = {}
    i = 0
    for event in events:
        time_event, number_train, type_event = event
        if type_event == TRAIN_IN:
            if len(stops_heap.heap) == 0:
                return [0, number_train]
            stop_number = stops_heap.extract()
            stops_train[number_train] = stop_number
        elif type_event == TRAIN_OUT:
            stop_number = stops_train[number_train]
            stops_heap.insert(stop_number)
        i += 1
        if i%40000 == 0:
            gc.collect()
    result_stops_train = []
    for number_train in sorted(stops_train.keys()):
        result_stops_train.append(stops_train[number_train])
    return result_stops_train


def main():
    # считываем входные данные
    k, trains = load_data(INPUT_FILE)
    # Расчет тупиков, куда придет поезд
    result_stops_train = calc_stop_train(k, trains)
    # Записываем результат в output.txt
    if result_stops_train[0] == 0:
        save_output(OUTPUT_FILE, " ".join(list(map(str, result_stops_train))))
    else:
        save_output(OUTPUT_FILE, "\n".join(list(map(str, result_stops_train))))


if __name__ == "__main__":
    main()
