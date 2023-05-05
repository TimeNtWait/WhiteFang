# https://contest.yandex.ru/contest/45469/problems/40/
# Дивизион  A
# 40. Сталкер
import math
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
# def load_data(filename):
#     with open(filename, "r") as file:
#         n, k = map(int, file.readline().split())
#         storage_map = []
#         # storage_map = set([])
#         for _ in range(k):
#             r = int(file.readline().strip())
#             edges = set([])
#             # edges = []
#             for _ in range(r):
#                 edges.add(map(int, file.readline().split()))
#                 # edges.append(map(int, file.readline().split()))
#             storage_map.append(edges)
#             # storage_map.add(edges)
#     return n, k, storage_map


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(filename):
    '''
    входные данные
    :n - кол-во зданий
    :k - кол-во карт
    :storage_map - массив карт, в каждой карте указаны ребра

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    # 1. Грузим все карты в граф
    # 2. Делаем обход ищем минимальный путь
    # 3. Считаем сколько карт использовали (предварительно сохрнаив соотношение ребро <=> карта)
    # Может быть что одно ребро в двух картах, тогда надо выбрать такую карту, которая дальше будет использоваться
    # Может быть несколько путей, придется делать два обхода: от старта до начала и обратно,
    # тогда найдем все ребра входящие в минимальный путь и из них уже надо будет выбрать оптимальную загрузку карт
    # Вариант 1
    #    После нахождения всех допустимых ребер можно пройтись еще раз обходом в ширину и уже искать минимальный взвешанный путь,
    #   для этого надо для каждого ребра понимать к какой карте оно относится и что произошел переход
    #   Надо учитывать ситуацию когда 1 и 2 ребро в одной карте а 2 и 3 в другой, на тертьем ребре надо плонимать что хоть,
    #   2 и 3 это одна карта но в пути от 1 до 3 все же была загрузка карты
    #   После можно пройтись еще раз
    # Вариант 2
    #   Можно изначально все вершины дополнительно помечать номером карты и для ребер которые переходные между картами указывать вес 1 для ребер внутри одной карты 1
    #   Т.е. от здания можно уйти к другому зданию на этой же карте за 0 или переключиться на другую карту на это же здание за 1
    #   И дальше обычный bfs
    # Вариант 3
    # вершины переходы можно помечать через дополнительную вершину -1, вход стоит 0 выход 1

    # Читаем данные из input.txt
    with open(filename, "r") as file:
        n, k = map(int, file.readline().split())
        n += 1
        # Формируем граф
        graph = {}
        ends = set([])
        bfs_queue = deque()
        vertexes = [math.inf] * ((n + 1) * (k + 1))
        # Заносим в граф ребра с одной карты
        for num_map in range(1, k + 1):
            n_num_map = num_map * n
            start_id = n_num_map + 1
            end_id = n_num_map + n - 1

            r = int(file.readline().strip())
            for _ in range(r):
                v1, v2 = map(int, file.readline().split())
                building1 = n_num_map + v1
                building2 = n_num_map + v2

                if building1 in graph:
                    graph[building1][building2] = 0
                    graph[building1][v1] = 0
                else:
                    graph[building1] = {building2: 0, v1: 0}

                if building2 in graph:
                    graph[building2][building1] = 0
                    graph[building2][v2] = 0
                else:
                    graph[building2] = {building1: 0, v2: 0}

                if v1 in graph:
                    graph[v1][building1] = 1
                else:
                    graph[v1] = {building1: 1}

                if v2 in graph:
                    graph[v2][building2] = 1
                else:
                    graph[v2] = {building2: 1}

            if start_id in graph.keys():
                bfs_queue.append(start_id)
                vertexes[start_id] = 1
            if end_id in graph.keys():
                ends.add(end_id)

    while len(bfs_queue) > 0:
        b1 = bfs_queue.popleft()
        for b2 in graph[b1]:
            new_val = vertexes[b1] + graph[b1][b2]
            if new_val < vertexes[b2]:
                vertexes[b2] = new_val
                if graph[b1][b2] == 1:
                    bfs_queue.append(b2)
                else:
                    bfs_queue.appendleft(b2)

    length_route = math.inf
    for end in ends:
        length_route = min(length_route, vertexes[end])

    if math.isinf(length_route):
        return -1
    else:
        return length_route


def main():
    # считываем входные данные
    # Поиск минимального пути
    length_route = find_path(INPUT_FILE)
    # print(length_route)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
