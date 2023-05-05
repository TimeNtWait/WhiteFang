# https://contest.yandex.ru/contest/46304/problems/C/
# C. Доставка со склада
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"

from collections import deque

import math


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        lost_times = []
        for _ in range(n):
            times = list(map(int, file.readline().split()))
            lost_times.append(times)
    return n, lost_times


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск ответа
def find_answer(n, lost_times):
    graph = {}
    pre_vertex = [(-1, -1)]
    graph[(-1, -1)] = {}
    visited = {}
    vertexes = {}
    vertexes[(-1, -1)] = (0, 0, -1)
    pre_sum = [(0,0)]
    for i, length in enumerate(lost_times):
        a, b = length
        v2_1 = (i, 1)
        v2_2 = (i, 2)
        visited[v2_1] = 0
        visited[v2_2] = 0
        for v1 in pre_vertex:
            # graph[v1][v2_1] = (pre_sum[i][0] + a, pre_sum[i][1])
            # graph[v1][v2_2] = (pre_sum[i][0], pre_sum[i][1] + b)
            graph[v1][v2_1] = (a, 0)
            graph[v1][v2_2] = (0, b)
        graph[v2_1] = {}
        graph[v2_2] = {}
        pre_vertex = [v2_1, v2_2]
        # pre_sum = [graph[v1][v2_1], graph[v1][v2_2]]
        vertexes[v2_1] = (math.inf, math.inf, -1)
        vertexes[v2_2] = (math.inf, math.inf, -1)
        # vertexes[v2_1] = (0, 0, -1)
        # vertexes[v2_2] = (0, 0, -1)

    # print(graph)

    start_point = (-1, -1)
    stack = [start_point]
    visited[start_point] = 1
    # vertexes = [[i for i in range(1, n)],[0],[]]
    while len(stack) > 0:
        select_v = stack.pop()
        new_color = 3 - visited[select_v]
        for v in graph[select_v]:
            new_len_1 = vertexes[vertex][0] + graph[vertex][v][0]
            new_len_2 = vertexes[vertex][1] + graph[vertex][v][1]
            if visited[v] == 0 and :

        # for vv in range(n):
        for ii in range(len(vertexes[0]) - 1, -1, -1):
            # print(f"ii: {ii}")
            vv = vertexes[0][ii]
            if visited[vv] == 0 and graph[select_v][vv] < check_length:
            # if graph[select_v][vertexes[0][ii]] < check_length:
            #     vv = vertexes[0][ii]
            #     get_item =
                vertexes[0].remove(vv)
                visited[vv] = new_color
                vertexes[new_color].append(vv)
                stack.append(vv)

        # for vv in vertexes[0]:
        # for ii in range(len(vertexes[0]) - 1, -1, -1):
        #     vv = vertexes[0][ii]
        #     visited[vv] = 1
        #     vertexes[1].append(vertexes[0].pop())
        #     stack.append(vv)

        if len(stack) == 0:
            for vv in  vertexes[0]:
                vertexes[0].remove(vv)
                vertexes[1].append(vv)
                visited[vv] = 1
                stack.append(vv)
                break


    assert False




    queue_bfs = deque()
    queue_bfs.append((-1, -1))
    # min_pare = [math.inf, math.inf]
    while len(queue_bfs) > 0:
        vertex = queue_bfs.popleft()
        for v in graph[vertex]:

            new_len_1 = vertexes[vertex][0] + graph[vertex][v][0]
            new_len_2 = vertexes[vertex][1] + graph[vertex][v][1]
            print(f"v: {v}, vertexes[v]: {vertexes[v]}")
            # if new_len_1 < new_len_2:
            #     vertexes[v] = (new_len_1, vertexes[v][1], vertex)
            # else:
            #     vertexes[v] = (vertexes[v][0], new_len_2, vertex)
            # queue_bfs.append(v)
            # assert False
            # # if max(new_len_1, new_len_2) < max(vertexes[v][0], vertexes[v][1]):
            # # if max(new_len_1, vertexes[v][1]) < max(vertexes[v][0], new_len_2):
            # #     vertexes[v] = (new_len_1, vertexes[v][1], vertex)
            # # else:
            # #     vertexes[v] = (vertexes[v][0], new_len_2, vertex)
            # # queue_bfs.append(v)
            #     # if new_len_2 < vertexes[v][1]:
            #     #     vertexes[v] = (vertexes[v][0], new_len_2, vertex)
            #     # vertexes[v] = (new_len_1, new_len_2, vertex)

            if max(new_len_1, new_len_2) < max(vertexes[v][0], vertexes[v][1]):
                # if new_len_1 < vertexes[v][0]:
                #     vertexes[v] = (new_len_1, vertexes[v][1], vertex)
                # if new_len_2 < vertexes[v][1]:
                #     vertexes[v] = (vertexes[v][0], new_len_2, vertex)
                vertexes[v] = (new_len_1, new_len_2, vertex)
                queue_bfs.append(v)



    path = []
    v1 = vertexes[(n - 1, 1)]
    v2 = vertexes[(n - 1, 2)]

    print(vertexes)
    print(v1)
    print(v2)

    if max(v1[:2]) < max(v2[:2]):
        last_vertex = v1[-1]
        path.append(1)
    else:
        last_vertex = v2[-1]
        path.append(2)

    for i in range(n - 2, -1, -1):
        v = vertexes[(i, last_vertex[-1])]
        path.append(last_vertex[-1])
        last_vertex = v[-1]

    path.reverse()
    return " ".join(map(str, path))


def main():
    # считываем входные данные
    n, lost_times = load_data(INPUT_FILE)
    # Поиск ответа
    answer = find_answer(n, lost_times)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(answer))


if __name__ == "__main__":
    main()
