# https://contest.yandex.ru/contest/46304/problems/C/
# C. Доставка со склада
# from sys import setrecursionlimit
# # Снимаем ограничеи на кол-во рекурсий
# setrecursionlimit(200000)
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
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
    for i, length in enumerate(lost_times):
        a, b = length
        v2_1 = (i, 1)
        v2_2 = (i, 2)
        visited[v2_1] = False
        visited[v2_2] = False
        for v1 in pre_vertex:
            graph[v1][v2_1] = (a,0)
            graph[v1][v2_2] = (0, b)
        graph[v2_1] = {}
        graph[v2_2] = {}
        pre_vertex = [v2_1, v2_2]
        vertexes[v2_1] = (math.inf, math.inf, -1)
        vertexes[v2_2] = (math.inf, math.inf, -1)

    def dfs(graph, vertex, visited, vertexes):
        for v in graph[vertex]:
            new_len_1 = vertexes[vertex][0] + graph[vertex][v][0]
            new_len_2 = vertexes[vertex][1] + graph[vertex][v][1]

            # print(f"v: {v} new_len_1: {new_len_1}, new_len_2: {new_len_2}, max(new_len_1, new_len_2): {max(new_len_1, new_len_2)}, max(vertexes[v][0], vertexes[v][1]):{max(vertexes[v][0], vertexes[v][1])}")
            # assert False
            if max(new_len_1, new_len_2) < max(vertexes[v][0], vertexes[v][1]):
                print(f"update vert {vertexes[v]}")
            # if new_len < vertexes[v][0]:
            #     vertexes[v] = (new_len_1, new_len_2, vertex[1])
                vertexes[v] = (new_len_1, new_len_2, vertex)
                print(f"v:{v}, vertexes[v]: {vertexes[v]}")
                # vertexes[v] = (new_len, vertex[1])
                dfs(graph, v, visited, vertexes)

    path = []
    dfs(graph, (-1, -1), visited, vertexes)

    print(vertexes)
    # print(vertexes[(n - 1, 1)], vertexes[(n - 1, 2)])
    v1 = vertexes[(n - 1, 1)]
    v2 = vertexes[(n - 1, 2)]
    # print(v1,v2)
    print(max(v1[:2]),max(v2[:2]))
    # print(max(v1[:1],v2)
    if max(v1[:2]) < max(v2[:2]):
        last_vertex = (n - 2, vertexes[(n - 1, 1)][-1])
        path.append(1)
    else:
        last_vertex = (n - 2, vertexes[(n - 1, 2)][-1])
        path.append(2)
    # print(f"last_vertex: {last_vertex}")
    # print(f"path: {path}")
    # assert False

    # if vertexes[(n - 1, 1)] < vertexes[(n - 1, 2)]:

    # if vertexes[(n - 1, 1)] < vertexes[(n - 1, 2)]:
    #     last_vertex = (n - 2, vertexes[(n - 1, 1)][1])
    #     path.append(1)
    # else:
    #     last_vertex = (n - 2, vertexes[(n - 1, 2)][1])
    #     path.append(2)
    #
    for i in range(n - 2, -1, -1):
        v = vertexes[(i, last_vertex[-1])]
        path.append(last_vertex[-1])
        last_vertex = (i - 1, v[-1])
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
