# https://contest.yandex.ru/contest/45468/problems/19/
# Дивизион B
# 19. Хипуй
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    commands = []
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        for _ in range(n):
            commands.append(file.readline().strip())
    return [c for c in commands]


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


class Heap():
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
                if self.heap[parent_index] < self.heap[index_new_item]:
                    self.heap[parent_index], self.heap[index_new_item] = self.heap[index_new_item], self.heap[
                        parent_index]
                    index_new_item = parent_index
                else:
                    break

    def extract(self):
        extract_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        index_change_item = 0
        while index_change_item < len(self.heap) - 2:
            index_children_left = (index_change_item + 1) * 2 - 1
            index_children_right = (index_change_item + 1) * 2

            if index_children_left >= len(self.heap) - 1:
                children_left = None
            else:
                children_left = self.heap[index_children_left]
            if index_children_right >= len(self.heap) - 1:
                children_right = None
            else:
                children_right = self.heap[index_children_right]

            if children_right is not None and children_right >= children_left and children_right > \
                    self.heap[index_change_item]:
                self.heap[index_change_item], self.heap[index_children_right] = self.heap[index_children_right], \
                                                                                self.heap[index_change_item]
                index_change_item = index_children_right
            elif children_left is not None and children_left > self.heap[index_change_item] and (
                    children_right is None or
                    children_left >= children_right):
                self.heap[index_change_item], self.heap[index_children_left] = self.heap[index_children_left], \
                                                                               self.heap[index_change_item]
                index_change_item = index_children_left
            else:
                break
        # Удаляем последний элемент, который изначально скопировали вначало списка
        self.heap.pop()
        return extract_item


def main():
    # считываем входные данные
    commands = load_data(INPUT_FILE)
    result_extract = []
    # Реализация Кучи - структура данных
    heap = Heap()
    for command in commands:
        if command[0] == "0":
            number = int(command.split()[1])
            heap.insert(number)
        elif command[0] == "1":
            result_extract.append(str(heap.extract()))
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(result_extract))


if __name__ == "__main__":
    main()
