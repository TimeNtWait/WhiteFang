# https://contest.yandex.ru/contest/45469/problems/34/
# Дивизион A
# 34. Десант
from sys import setrecursionlimit
# Снимаем ограничеи на кол-во рекурсий
setrecursionlimit(200000)

from threading import stack_size
mb = 1024 * 1024
stack_size(128 * mb)


INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        map_table = []
        for _ in range(n):
            row = file.readline().split()
            map_table.append(list(map(int, row)))
    return n, m, map_table


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

# Ищем локальные минимумы
def dfs(map_table, graph, vertex, visited, local_point):
    # print(f"vertex:{vertex}")
    # print(f"graph[vertex]:{graph[vertex]}")
    for v in graph[vertex]:
        if map_table[v[0]][v[1]] >= map_table[vertex[0]][vertex[1]]:
            if not visited[v]:
                visited[v] = True
                # assert False
                # if map_table[v[0]][v[1]] < map_table[local_point[0]][local_point[1]]:
                #     local_point = v
                if v in graph:
                    local_point = dfs(map_table, graph, v, visited, local_point)
    return local_point


# Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
def dfs_stack(map_table, graph, vertex, visited, local_point):
    stack = [vertex]
    while len(stack) > 0:
        select_v = stack.pop()
        if map_table[select_v[0]][select_v[1]] >= map_table[vertex[0]][vertex[1]]:
            if not visited[select_v]:
                visited[select_v] = True
            # if map_table[select_v[0]][select_v[1]] < map_table[local_point[0]][local_point[1]]:
            #     local_point = select_v
        # visited[select_v] = True
                for vv in graph[select_v]:
                    if vv in graph:
                        # if not visited[vv]:
                        #     visited[vv] = True
                        stack.append(vv)
    return local_point


# # Ищем локальные минимумы
# def dfs(map_table, graph, vertex, visited, local_point):
#     for v in graph[vertex]:
#         if not visited[v]:
#             visited[v] = True
#             if map_table[v[0]][v[1]] < map_table[local_point[0]][local_point[1]]:
#                 local_point = v
#             if v in graph:
#                 local_point = dfs(map_table, graph, v, visited, local_point)
#     return local_point
#
# # Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
# def dfs_stack(map_table, graph, vertex, visited, local_point):
#     stack = [vertex]
#     while len(stack) > 0:
#         select_v = stack.pop()
#         if map_table[select_v[0]][select_v[1]] < map_table[local_point[0]][local_point[1]]:
#             local_point = select_v
#
#         visited[select_v] = True
#         for vv in graph[select_v]:
#             if vv in graph:
#                 if not visited[vv]:
#                     visited[vv] = True
#                     stack.append(vv)
#     return local_point





# Схлопываем одинаковые минимумы
def dfs_join(graph, vertex, visited):
    if vertex not in graph:
        return
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            dfs_join(graph, v, visited)


# Посчет минимального кол-ва ловушек
def calc_catch(n, m, map_table):
    '''
    входные данные
    :n, m  — размеры карты
    :map_table — матрица карты с указанием высот

    выходные данные
    :count_catch – количество пустых клеток в данной комнате.
    '''
    if n == 0 or m == 0:
        return "0"

    visited = {}
    graph = {}
    min_val = max_val = map_table[0][0]
    for i in range(n):
        for j in range(m):
            min_val = min(min_val, map_table[i][j])
            max_val = max(max_val, map_table[i][j])
            point = (i, j)
            visited[point] = False
            open_cells = get_open_cells(map_table, point)
            if point not in graph:
                graph[point] = []
            for p in open_cells:
                graph[point].append(p)
    if min_val == max_val:
        return "1"
    print(f"graph:{graph}")

    # Ищем локальные минимумы
    print(f"# Ищем локальные минимумы")
    vertexes = []
    visited_local = visited.copy()
    copy_visited = visited.copy()
    for p in graph.keys():
        # print(p)
        # local_point = dfs(map_table, graph, p, copy_visited, p)
        # if not copy_visited[p]:
        #     local_point = dfs(map_table, graph, p, copy_visited, p)
        #     copy_visited[p] = True

        if not copy_visited[p]:
            # local_point = dfs(map_table, graph, p, copy_visited, p)
            local_point = dfs_stack(map_table, graph, p, copy_visited, p)
            copy_visited[p] = True




        # print(f"copy_visited: {copy_visited}")

        # assert False
        # copy_visited = visited_local.copy()
        # copy_visited = visited_local.copy()
        # local_point = dfs_stack(map_table, graph, p, copy_visited, p)
        # visited_local[p] = True
        # visited_local[local_point] = False

        vertexes.append(local_point)
    vertexes = set(vertexes)

    visited = {}
    for i in range(n):
        for j in range(m):
            if (i, j) in vertexes:
                visited[(i, j)] = False
            else:
                visited[(i, j)] = True

    print(f"# Схлопываем одинаковые минимумы")
    # Схлопываем одинаковые минимумы
    res_vertexes = []
    for p in vertexes:
        if not visited[p]:
            res_vertexes.append(p)
            dfs_join(graph, p, visited)
    print(f"res_vertexes: {res_vertexes}, len(res_vertexes): {len(res_vertexes)}")
    return len(res_vertexes)


def main():
    # считываем входные данные
    n, m, map_table = load_data(INPUT_FILE)
    # Посчет минимального кол-ва ловушек
    count_catch = calc_catch(n, m, map_table)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_catch))


if __name__ == "__main__":
    main()
