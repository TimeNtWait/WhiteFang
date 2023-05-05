# https://contest.yandex.ru/contest/45468/problems/36/
# Дивизион  B
# 36. Длина кратчайшего пути
from collections import deque
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        graph_matrix = []
        for _ in range(n):
            graph_matrix.append(list(map(int, file.readline().split())))
        begin, end = map(int, file.readline().split())
    return n, graph_matrix, begin, end


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Формируем граф из матрицы смежности
def create_orient_graph(n, graph_matrix):
    graph = {}
    for i in range(n):
        for j in range(n):
            if graph_matrix[i][j] != 0:
                v1 = i + 1
                v2 = j + 1
                if v1 in graph:
                    graph[v1].append(v2)
                else:
                    graph[v1] = [v2]
    return graph


# Поиск длины кратчайшего пути
def find_cycle(n, graph_matrix, begin, end):
    '''
    входные данные
    :n — количество вершин в графе
    :graph_matrix — матрица смежности
    :begin - начальная вершина
    :end - конечная вершина

    выходные данные
    :length_route - Длина кратчайшего пути
    '''

    graph = create_orient_graph(n, graph_matrix)
    queue_bfs = deque()
    queue_bfs.append(begin)

    len_path = {}
    for i in range(n):
        len_path[i + 1] = math.inf
    len_path[begin] = 0
    # обход в ширину
    while len(queue_bfs) > 0:
        vertex = queue_bfs.pop()
        if vertex in graph:
            for v in graph[vertex]:
                if len_path[vertex] + 1 < len_path[v]:
                    len_path[v] = len_path[vertex] + 1
                    queue_bfs.append(v)
    if math.isinf(len_path[end]):
        return -1
    else:
        return len_path[end]


def main():
    # считываем входные данные
    n, graph_matrix, begin, end = load_data(INPUT_FILE)
    # Поиск длины кратчайшего пути
    length_route = find_cycle(n, graph_matrix, begin, end)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
