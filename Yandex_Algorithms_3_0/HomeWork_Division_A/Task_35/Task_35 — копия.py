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


# Определяем доступные ячейки
def get_open_cells(map_table, point):
    n = len(map_table)
    m = len(map_table[0])
    open_cells = []
    x, y = point
    if x > 0 and map_table[x - 1][y] >= map_table[x][y]:
        open_cells.append((x - 1, y))

    if x + 1 < n and map_table[x + 1][y] >= map_table[x][y]:
        open_cells.append((x + 1, y))

    if y > 0 and map_table[x][y - 1] >= map_table[x][y]:
        open_cells.append((x, y - 1))
    if y + 1 < m and map_table[x][y + 1] >= map_table[x][y]:
        open_cells.append((x, y + 1))
    return open_cells


# from sys import setrecursionlimit
# # Снимаем ограничеи на кол-во рекурсий
# setrecursionlimit(200000)
# Ищем локальные минимумы
# def dfs(map_table, graph, vertex, visited, local_point):
#
#     for v in graph[vertex]:
#         if map_table[v[0]][v[1]] >= map_table[vertex[0]][vertex[1]]:
#             if not visited[v]:
#                 visited[v] = True
#                 if v in graph:
#                     local_point = dfs(map_table, graph, v, visited, local_point)
#     return local_point

def check_local_minimum(map_table, point):
    n = len(map_table)
    m = len(map_table[0])
    x1, y1 = point
    val = map_table[x1][y1]
    if x1 > 0:
        val = min(val, map_table[x1 - 1][y1])
    if x1 + 1 < n:
        val = min(val, map_table[x1 + 1][y1])
    if y1 > 0:
        val = min(val, map_table[x1][y1-1])
    if y1 + 1 < m:
        val = min(val, map_table[x1][y1+1])
    return val


# # Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
# # Ищем локальные минимумы
# def dfs_stack(map_table, graph, vertex, visited, mini):
#     stack = [vertex]
#     x, y = vertex
#     while len(stack) > 0:
#         select_v = stack.pop()
#         if map_table[select_v[0]][select_v[1]] ==  map_table[x][y]:
#             mini = min(mini, check_local_minimum(map_table, select_v))
#         if map_table[select_v[0]][select_v[1]] >= map_table[x][y]:
#             if not visited[select_v]:
#                 visited[select_v] = True
#                 for vv in graph[select_v]:
#                     if vv in graph:
#                         stack.append(vv)
#     return mini
#

# # Схлопываем одинаковые минимумы
# def dfs_join(graph, vertex, visited):
#     if vertex not in graph:
#         return
#     for v in graph[vertex]:
#         if not visited[v]:
#             visited[v] = True
#             dfs_join(graph, v, visited)
#

# Формируем граф из списка ребер
def create_orient_graph(courses):
    graph= {}
    for i in range(len(courses)):
        graph[i + 1] = []
    for i, course in enumerate(courses):
        for c in course:
            graph[c].append(i + 1)
    return graph

# Производим топологическую сортировку
def dfs(graph, vertex, visited, vertexes):
    # print(f"vertex:{vertex}")
    for v in graph[vertex]:
        # print(graph[vertex])
        # print(f"v:{v}")
        if not visited[v]:
            dfs(graph, v, visited, vertexes)
            visited[v] = True
            vertexes.append(v)
    # vertexes.append(graph[vertex])


# Составление расписания по прохождению курсов
def sort_courses(n, courses):
    '''
    входные данные
    :n  — кол-во курсов
    :courses — список курсов. Первое значение это кол-во курсов, далее их требования по колву пройденых ранее курсов

    выходные данные
    :sorted_courses – количество пустых клеток в данной комнате.
    '''
    print(n, courses)
    sorted_courses = ""
    if n == 0:
        return ""

    # Составляем ориентированый граф
    graph = create_orient_graph(courses)

    print(f"graph: {graph}")
    # Сортируем расположение вершин в графе для более оптимального распределения
    for key in graph.keys():
        # graph[key] = sorted(graph[key], reverse=True)
        graph[key] = sorted(graph[key], reverse=True)
    # weights = {}
    # for c in range(1, n+1):
    #     weights[c] = n**(c-1)*c
    src_visited = {}
    for v in range(1, n + 1):
        src_visited[v] = False

    # Производим топологическую сортировку
    vertexes = []
    # for v in range(n, 0, -1):
    all_vertexes = []
    for v in range(1, n + 1):
        visited = src_visited.copy()
        vertexes = []
        if not visited[v]:
            dfs(graph, v, visited, vertexes)
            vertexes.append(v)
            visited[v] = True
        vertexes.reverse()
        all_vertexes.append(vertexes)
        print(f"v: {v}, vertexes: {vertexes}")

    # vertexes.reverse()
    print(f"vertexes: {vertexes}")
    sorted_courses = []
    print(f"all_vertexes:{all_vertexes}")
    # for i in range(n):
    while len(sorted_courses) < n:
        # print(f"i :{i}")
        max_item = 0
        for v in all_vertexes:
            # max_item = max(max_item, v[-1-i])
            while len(v) > 0 and v[-1] in sorted_courses:
                v.pop()
            if len(v) > 0:
                max_item = max(max_item, v[-1])

                # print(f"v:{v}, v[-1-i]: {v[-1-i]}")
        # for v in all_vertexes:
        #     # while len(v) > 0 and v[-1] >= max_item:
        #     #     v.pop()
        #     if len(v) > 0:
        #         if v[-1] >= max_item:
        #             v.pop()
        if max_item > 0 and max_item not in sorted_courses:
            print(f"max_item:{max_item}")
            sorted_courses.append(max_item)
    print(f"all_vertexes:{all_vertexes}")
    sorted_courses.reverse()
    print(f"sorted_courses: {sorted_courses}")
    return " ".join(map(str, sorted_courses))



    # if n == 0 or m == 0:
    #     return "0"
    #
    # visited = {}
    # graph = {}
    # for i in range(n):
    #     for j in range(m):
    #         point = (i, j)
    #         visited[point] = False
    #         open_cells = get_open_cells(map_table, point)
    #         if point not in graph:
    #             graph[point] = []
    #         for p in open_cells:
    #             graph[point].append(p)
    #
    # # Ищем локальные минимумы
    # vertexes = set([])
    # for p in graph.keys():
    #     if not visited[p]:
    #         local_min = dfs_stack(map_table, graph, p, visited, map_table[p[0]][p[1]])
    #         if local_min == map_table[p[0]][p[1]]:
    #             vertexes.add(p)
    #
    # visited = {}
    # for i in range(n):
    #     for j in range(m):
    #         if (i, j) in vertexes:
    #             visited[(i, j)] = False
    #         else:
    #             visited[(i, j)] = True
    #
    # # Схлопываем одинаковые минимумы
    # res_vertexes = set([])
    # for p in vertexes:
    #     if not visited[p]:
    #         res_vertexes.add(p)
    #         dfs_join(graph, p, visited)
    # # print(f"res_vertexes:{res_vertexes}")
    # return len(res_vertexes)


def main():
    # считываем входные данные
    n, courses = load_data(INPUT_FILE)
    # Составление расписания по прохождению курсов
    sorted_courses = sort_courses(n, courses)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sorted_courses))


if __name__ == "__main__":
    main()
