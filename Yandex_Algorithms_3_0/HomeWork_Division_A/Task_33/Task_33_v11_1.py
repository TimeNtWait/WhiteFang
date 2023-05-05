# https://contest.yandex.ru/contest/45469/problems/33/
# Дивизион A
# 33. Радио Байтик
from sys import setrecursionlimit

# Снимаем ограничеи на кол-во рекурсий
setrecursionlimit(200000)
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        points = []
        for _ in range(n):
            points.append(tuple(map(int, file.readline().split())))
    return n, points


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет требуемой мощности между двумя вышками
def calc_power(p1, p2):
    # расчет расстояния между вышками.
    # Для ускорения итоговые расчеты будут произведены в самом конце над итогоовым значением
    l = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    return l


# # Пытаемся раскрасить граф в два цвета
# def dfs(graph, visited, vertexes, vertex, color, check_length):
#     if vertex not in graph:
#         return
#     for v in graph[vertex]:
#         if visited[v] == 0 and graph[vertex][v] < check_length:
#             visited[v] = 3 - color
#             vertexes.append(v)
#             dfs(graph, visited, vertexes, v, visited[v], check_length)

# # Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
def dfs_stack(graph, n, visited, vertex, check_length):
    stack = [vertex]
    while len(stack) > 0:
        select_v = stack.pop()
        new_color = 3 - visited[select_v]
        for vv in range(n):
            if visited[vv] == 0 and graph[select_v][vv] < check_length:
                visited[vv] = new_color
                stack.append(vv)
        if len(stack) == 0:
            if 0 in visited:
                vv = visited.index(0)
                visited[vv] = 1
                stack.append(vv)


# Расчет оптимальной мощности радио
def calc_radio_power(n, points):
    '''
    входные данные
    :n — количество вышек
    :points — координаты вышек

    выходные данные
    :radio_power – оптимальная мощность радио
    '''
    # Формируем полный граф
    # graph = {}
    graph = [[-1] * n for _ in range(n)]
    src_visited = [-1] * n
    lengths = set([])
    for i in range(n - 1):
        if src_visited[i] == -1:
            src_visited[i] = 0
        for j in range(i + 1, n):
            if src_visited[j] == -1:
                src_visited[j] = 0
            l = calc_power(points[i], points[j])
            graph[i][j] = l
            graph[j][i] = l
            lengths.add(l)
    src_visited[0] = 1
    lengths = list(lengths)
    lengths.sort()

    def check_valid_length(graph, n, visited, check_length):
        for i in range(n-1):
            for j in range(i+1,n):
                if visited[i] == visited[j] and graph[i][j] < check_length:
                    return  False
        return True

    l = 0
    r = len(lengths)
    true_length = 0
    true_choice = []
    while l < r:
        m = (l + r + 1) // 2
        check_length = lengths[m]
        visited = src_visited.copy()
        # dfs_stack(graph, n, visited, 0, check_length)
        # buffer = set([i for i in range(n)])

        stack = [0]
        vertexes = [[i for i in range(1, n)],[0],[]]
        while len(stack) > 0:
            select_v = stack.pop()
            new_color = 3 - visited[select_v]
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

                # for vv in vertexes[0]:
                #     print(f"vv1: {vv}")
                # if 0 in visited:
                #     print(f"vv2: {vv}")
                #     vv = visited.index(0)
                #     visited[vv] = 1
                #     stack.append(vv)
            # if len(stack) == 0:
            #     print(f"vertexes: {vertexes}")
            #     assert False
            #     if 0 in visited:
            #         vv = visited.index(0)
            #         visited[vv] = 1
            #         stack.append(vv)
            #
        is_check = check_valid_length(graph, n, visited, check_length)
        if is_check:
            l = m
            true_length = lengths[m]
            true_choice = visited.copy()
        else:
            r = m - 1
    true_length = round((true_length ** (1 / 2)) / 2, 15)
    radio_power = f"{true_length}\n" + " ".join(map(str, true_choice))
    print(f"radio_power:{radio_power}")
    return radio_power


def main():
    # считываем входные данные
    n, points = load_data(INPUT_FILE)
    # Расчет оптимальной мощности радио
    radio_power = calc_radio_power(n, points)

    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_radio_power)
    # radio_power = lp_wrapper(n, points)
    # lp.print_stats()

    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(radio_power))


if __name__ == "__main__":
    main()
    # import time
    # start_time = time.time()
    # main()
    # # print(f"length_route: {length_route}")
    # print(time.time() - start_time)
