# https://contest.yandex.ru/contest/45469/problems/35/
# Дивизион A
# 35. Кружки в Маховниках
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        courses = []
        for _ in range(n):
            row = file.readline().split()
            row = list(map(int, row))
            courses.append(row[1:])
    return n, courses


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
        size_heap = len(self.heap)
        while index_change_item < len(self.heap) - 2:
            index_children_left = (index_change_item + 1) * 2 - 1
            index_children_right = (index_change_item + 1) * 2

            if index_children_right > size_heap - 1 or index_children_left > size_heap - 1:
                break
            children_left = self.heap[index_children_left]
            children_right = self.heap[index_children_right]

            if children_right >= children_left and children_right > self.heap[index_change_item]:
                self.heap[index_change_item], self.heap[index_children_right] = self.heap[index_children_right], \
                                                                                self.heap[index_change_item]
                index_change_item = index_children_right
            elif children_left > self.heap[index_change_item] and children_left >= children_right:
                self.heap[index_change_item], self.heap[index_children_left] = self.heap[index_children_left], \
                                                                               self.heap[index_change_item]
                index_change_item = index_children_left
            else:
                break
        # Удаляем последний элемент, который изначально скопировали вначало списка
        self.heap.pop()
        return extract_item

# Формируем граф из списка ребер
def create_orient_graph(courses):
    # Считаем кол-во родителей у вершины
    parent_counts = {}
    #reverse_parent_counts = {}
    graph = {}
    # reverse_graph = {}
    for i in range(len(courses)):
        # graph[i + 1] = []
        graph[i + 1] = []
        parent_counts[i + 1] = 0
    for i, course in enumerate(courses):
        for c in course:
            # graph[c].append(i + 1)
            graph[i + 1].append(c)
            # Считаем кол-во потомков у вершин
            parent_counts[c] += 1
    return graph, parent_counts



# Составление расписания по прохождению курсов
def sort_courses(n, courses):
    '''
    входные данные
    :n  — кол-во курсов
    :courses — список курсов. Первое значение это кол-во курсов, далее их требования по колву пройденых ранее курсов

    выходные данные
    :sorted_courses – количество пустых клеток в данной комнате.
    '''
    if n == 0:
        return ""

    # Составляем ориентированый граф
    graph, parent_counts = create_orient_graph(courses)



    # Формируем кучу для хранения вершин по максимальному значнию
    heap_vertex = Heap()
    for v in parent_counts.keys():
        if parent_counts[v] == 0:
            heap_vertex.insert(v)
    sorted_courses = []
    i = 0
    while len(heap_vertex.heap) > 0:
        vertex = heap_vertex.extract()
        sorted_courses.append(vertex)
        for v in graph[vertex]:
            parent_counts[v] -= 1
            if parent_counts[v] == 0:
                heap_vertex.insert(v)
    sorted_courses.reverse()
    print(f"sorted_courses: {sorted_courses}")
    return " ".join(map(str, sorted_courses))


def main():
    # считываем входные данные
    n, courses = load_data(INPUT_FILE)
    # Составление расписания по прохождению курсов
    sorted_courses = sort_courses(n, courses)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sorted_courses))


if __name__ == "__main__":
    main()
