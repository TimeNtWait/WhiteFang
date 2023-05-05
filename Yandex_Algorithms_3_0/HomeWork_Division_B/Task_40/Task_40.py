# https://contest.yandex.ru/contest/45468/problems/40/
# Дивизион  B
# 40. Метро
from collections import deque
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        m = int(file.readline().strip())
        lines = []
        for _ in range(m):
            stations = list(map(int, file.readline().split()))
            lines.append(stations[1:])
        start, end = map(int, file.readline().split())
    return n, m, lines, start, end


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(n, m, lines, start, end):
    '''
    входные данные
    :n - кол-во станций метро
    :m - кол-во линий метро
    :lines - массив станций по каждой линии
    :start - начальная станция
    :end - конечная станция

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    # создаем 0-1 граф метро, где ребра для станций одной линии будут 0, а пересадки 1
    graph = {}
    start_list = []
    end_list = []
    vertexes = {}
    for i, line in enumerate(lines):
        for i_l1 in range(len(line)):
            s1 = line[i_l1]
            station1 = (s1, i)
            vertexes[station1] = math.inf
            graph[station1] = {}
            if s1 == start:
                start_list.append(station1)
            if s1 == end:
                end_list.append(station1)
            neighbor = []
            if i_l1 > 0:
                neighbor.append(i_l1 - 1)
            if i_l1 < len(line) - 1:
                neighbor.append(i_l1 + 1)
            for i_l2 in neighbor:
                s2 = line[i_l2]
                station2 = (s2, i)
                graph[station1][station2] = 0
                if station2 not in graph:
                    graph[station2] = {}
                graph[station2][station1] = 0
            for j, line2 in enumerate(lines):
                if i != j and s1 in line2:
                    graph[station1][(s1, j)] = 1
                    if (s1, j) not in graph:
                        graph[(s1, j)] = {}
                    graph[(s1, j)][station1] = 1

    queue_bfs = deque()
    for start_st in start_list:
        queue_bfs.append(start_st)
        vertexes[start_st] = 0
    while len(queue_bfs) > 0:
        st1 = queue_bfs.popleft()
        for st2 in graph[st1]:
            if st2 in graph[st1]:
                if vertexes[st1] + graph[st1][st2] < vertexes[st2]:
                    vertexes[st2] = vertexes[st1] + graph[st1][st2]
                    queue_bfs.append(st2)
    length_route = math.inf
    for end_st in end_list:
        length_route = min(length_route, vertexes[end_st])
    if math.isinf(length_route):
        return -1
    else:
        return length_route


def main():
    # считываем входные данные
    n, m, lines, start, end = load_data(INPUT_FILE)
    # Поиск минимального пути
    length_route = find_path(n, m, lines, start, end)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
