# https://contest.yandex.ru/contest/45469/problems/16/
# Дивизион А
# 16. Минимум на отрезке
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, k = map(int, file.readline().split())
        sequence = list(map(int, file.readline().split()))
    return n, k, sequence


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


class HeapMin():
    def __init__(self):
        self.heap = []
        self.values_position = {}

    def size(self):
        return len(self.heap)

    def fix_position(self, value, pos):
        if value in self.values_position:
            self.values_position[value].append(pos)
        else:
            self.values_position[value] = [pos]

    def change_position(self, value, old_pos, new_pos):
        index_position = self.values_position[value].index(old_pos)
        self.values_position[value][index_position] = new_pos

    def remove_position(self, value, pos):
        del_index = self.values_position[value].index(pos)
        del self.values_position[value][del_index]

    def check_heap(self, pos):
        while pos > 0:
            parent_index = (pos + 1) // 2 - 1
            if self.heap[parent_index] > self.heap[pos]:
                self.change_position(self.heap[parent_index], parent_index, pos)
                self.change_position(self.heap[pos], pos, parent_index)

                self.heap[parent_index], self.heap[pos] = self.heap[pos], self.heap[
                    parent_index]
                pos = parent_index
            else:
                break

    def insert(self, n):
        if self.size() == 0:
            self.heap.append(n)
            self.fix_position(n, 0)
        else:

            self.heap.append(n)
            index_new_item = len(self.heap) - 1
            self.fix_position(n, index_new_item)
            self.check_heap(index_new_item)

    def remove(self, value):
        remove_index = self.values_position[value][0]
        self.remove_position(value, remove_index)
        if len(self.values_position[value]) == 0:
            self.values_position.pop(value)
        self.heap[remove_index] = self.heap[-1]
        if remove_index < len(self.heap) - 1:
            self.change_position(self.heap[-1], len(self.heap) - 1, remove_index)
        self.check_heap(remove_index)
        while remove_index < len(self.heap) - 2:
            index_children_left = (remove_index + 1) * 2 - 1
            index_children_right = (remove_index + 1) * 2
            if index_children_left >= len(self.heap) - 1:
                children_left = None
            else:
                children_left = self.heap[index_children_left]
            if index_children_right >= len(self.heap) - 1:
                children_right = None
            else:
                children_right = self.heap[index_children_right]

            if children_right is not None and children_right <= children_left and children_right <= \
                    self.heap[remove_index]:
                self.change_position(self.heap[remove_index], remove_index, index_children_right)
                self.change_position(self.heap[index_children_right], index_children_right, remove_index)

                self.heap[remove_index], self.heap[index_children_right] = self.heap[index_children_right], \
                                                                           self.heap[remove_index]
                remove_index = index_children_right
            elif children_left is not None and children_left <= self.heap[remove_index] and (
                    children_right is None or
                    children_left <= children_right):
                self.change_position(self.heap[remove_index], remove_index, index_children_left)
                self.change_position(self.heap[index_children_left], index_children_left, remove_index)

                self.heap[remove_index], self.heap[index_children_left] = self.heap[index_children_left], \
                                                                          self.heap[remove_index]
                remove_index = index_children_left
            else:
                break
        # Удаляем последний элемент, который изначально скопировали вначало списка
        self.heap.pop()
        return value


# Поиск минимума в окне
def find_min_by_frame(n, k, sequence):
    '''
    входные данные
    :n — длинна входной последовательности
    :k — размер окна для поиск минимума
    :sequence - входная последовательность чисел

    выходные данные
    :min_by_frame - минимумы найденные в последовательности для заданного окна
    '''
    heap = HeapMin()
    for item in sequence[:k]:
        heap.insert(item)

    min_by_frame = [heap.heap[0]]
    for i in range(1, len(sequence) - k + 1):
        heap.remove(sequence[i - 1])
        heap.insert(sequence[i + k - 1])
        min_by_frame.append(heap.heap[0])
    return min_by_frame


def main():
    # считываем входные данные
    n, k, sequence = load_data(INPUT_FILE)
    # Поиск минимума в окне
    min_by_frame = find_min_by_frame(n, k, sequence)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(list(map(str, min_by_frame))))


if __name__ == "__main__":
    main()
