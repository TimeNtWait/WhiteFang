# https://contest.yandex.ru/contest/45469/problems/18/
# Дивизион А
# 18. Тупики
# import gc
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
    return n, k, trains


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


# Расчет тупиков, куда придет поезд
def calc_stop_train(n, k, trains):
    '''
    входные данные
    :n — количество поездов
    :k — количество тупиков
    :trains (time_in, time_out) — время прибытия и отправления электрички

    выходные данные
    :result_stops_train - список гобилнов зашедших к шаману
    '''
    stops_heap = HeapMin()
    create_size_heap = min(k, n, 100)
    max_number_stop = create_size_heap
    limit_size_heap = k - create_size_heap
    for i in range(create_size_heap):
        stops_heap.insert(i + 1)

    events = []
    for number_train, (time_in, time_out) in enumerate(trains):
        events.append((time_in, number_train + 1, TRAIN_IN))
        events.append((time_out + 1, number_train + 1, TRAIN_OUT))
    events = sorted(events)
    stops_train = {}
    list_stops_train = []
    # i = 0
    for _, number_train, type_event in events:
        size_heap = len(stops_heap.heap)
        if type_event == TRAIN_IN:
            if size_heap == 0:
                return [0, number_train]
            stop_number = stops_heap.extract()
            stops_train[number_train] = stop_number
            list_stops_train.append(stop_number)
        elif type_event == TRAIN_OUT:
            stop_number = stops_train[number_train]
            stops_train.pop(number_train)
            stops_heap.insert(stop_number)
        # Расширяем кучу по мере её используемости. Сразу кучу большого объема делать неэкономно по памяти
        if size_heap < 30:
            create_size_heap = min(limit_size_heap, 100)
            limit_size_heap = limit_size_heap - create_size_heap
            for i in range(create_size_heap):
                stops_heap.insert(max_number_stop + i + 1)
            max_number_stop += create_size_heap
        # i += 1
        # if i%20000 == 0:
        #     gc.collect()
    # result_stops_train = []
    # for number_train in sorted(stops_train.keys()):
    #     result_stops_train.append(stops_train[number_train])
    # return result_stops_train
    return list_stops_train


def main():
    # считываем входные данные
    n, k, trains = load_data(INPUT_FILE)
    # Расчет тупиков, куда придет поезд
    result_stops_train = calc_stop_train(n, k, trains)
    # Записываем результат в output.txt
    if result_stops_train[0] == 0:
        save_output(OUTPUT_FILE, " ".join(list(map(str, result_stops_train))))
    else:
        save_output(OUTPUT_FILE, "\n".join(list(map(str, result_stops_train))))


if __name__ == "__main__":
    main()
