# https://contest.yandex.ru/contest/45469/problems/34/
# Дивизион A
# 34. Десант
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


def get_open_cells(map_table, point, visited):
    n = len(map_table)
    m = len(map_table[0])
    open_cells = []
    x, y = point
    if (x - 1, y) not in visited:
        visited[(x - 1, y)] = False
    if (x + 1, y) not in visited:
        visited[(x + 1, y)] = False
    if (x, y - 1) not in visited:
        visited[(x, y - 1)] = False
    if (x, y + 1) not in visited:
        visited[(x, y + 1)] = False

    if x > 0 and map_table[x - 1][y] <= map_table[x][y] and not visited[(x - 1, y)]:
        open_cells.append((x - 1, y))

    if x + 1 < n and map_table[x + 1][y] <= map_table[x][y] and not visited[(x + 1, y)]:
        open_cells.append((x + 1, y))

    if y > 0 and map_table[x][y - 1] <= map_table[x][y] and not visited[(x, y - 1)]:
        open_cells.append((x, y - 1))
    if y + 1 < m and map_table[x][y + 1] <= map_table[x][y] and not visited[(x, y + 1)]:
        open_cells.append((x, y + 1))
    return open_cells


def check_local_minimum(map_table, point, visited):
    n = len(map_table)
    m = len(map_table[0])
    x, y = point
    if_list = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for add_i, add_j in if_list:
        if 0 <= x + add_i < n and 0 <= y + add_j < m:
            if map_table[x + add_i][y + add_j] < map_table[x][y]:
                return False
    return True


def dfs(map_table, point, visited, local_minimum):
    open_cells = get_open_cells(map_table, point, visited)
    for p in open_cells:
        if p not in visited:
            visited[p] = False

    # is_local_minimum = check_local_minimum(map_table, point, visited)

    # if len(open_cells) == 0 and is_local_minimum:
    if len(open_cells) == 0:
        print(f"point, local:{point}")
        # print(f"is_local_minimum: {is_local_minimum}")
        local_minimum.append(point)
        return

    for v in open_cells:
        if not visited[v]:
            visited[v] = True
            dfs(map_table, v, visited, local_minimum)
    # graph[point] = open_cells
    # for v in graph[point]:
    #     if not visited[v]:
    #         visited[v] = True
    #         dfs(map_table, graph, v, visited)


# Посчет минимального кол-ва ловушек
def calc_catch(n, m, map_table):
    '''
    входные данные
    :n, m  — размеры карты
    :map_table — матрица карты с указанием высот

    выходные данные
    :count_catch – количество пустых клеток в данной комнате.
    '''
    print(n, m, map_table)
    for i in range(n):
        print(map_table[i])

    map_downs = [[False] * m for _ in range(n)]
    # print(map_downs)
    # assert False

    if n == 0 or m == 0:
        return "0"

    visited = {}
    graph = {}
    for i in range(n):
        for j in range(m):
            point = (i, j)
            visited[point] = False
            print(f"i, j:{(i, j)}, point: {map_table[i][j]}")
            open_cells = get_open_cells(map_table, point, visited)
            print(f"open_cells: {open_cells}")
            if point not in graph:
                graph[point] = []
            is_neighbor_gt = True
            for p in open_cells:
                graph[point].append(p)
                if map_table[i][j] > map_table[p[0]][p[1]]:
                    is_neighbor_gt = False
            map_downs[i][j] = is_neighbor_gt

    print(f"graph: {graph}")
    print(f"map_downs: {map_downs}")

    # for i in range(n):
    #     for j in range(m):
    #
    # print(f"map_downs: {map_downs}")

    # assert False
    def dfs(map_table, graph, vertex, visited, local_point):
        if vertex not in graph:
            return
        is_local_minimum = True
        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                if map_table[v[0]][v[1]] < map_table[local_point[0]][local_point[1]]:
                    local_point = v
                # vertexes.append(v)
                local_point = dfs(map_table, graph, v, visited, local_point)
        return local_point

        # if is_local_minimum and is_lt and map_downs[vertex[0]][vertex[1]]:

    vertexes = []
    # copy_visited = visited.copy()
    # local_point = (3,3)
    # local_point = dfs(map_table, graph, (3,3), copy_visited, local_point)
    # print(f"local_point:{local_point}")
    #
    # return ""
    for p in graph.keys():
        copy_visited = visited.copy()
        local_point = dfs(map_table, graph, p, copy_visited, p)
        print(f"p :{p} local_point:{local_point}")
        vertexes.append(local_point)
    print(f"vertexes:{set(vertexes)}")
    vertexes = set(vertexes)

    visited = {}
    for i in range(n):
        for j in range(m):
            if (i,j) in vertexes:
                visited[(i,j)] = False
            else:
                visited[(i,j)] = True
    print(visited)

    # Схлопываем одинаковые минимумы
    def dfs_join(graph, vertex, visited):
        if vertex not in graph:
            return
        for v in graph[vertex]:
            if not visited[v]:
                visited[v] = True
                dfs_join( graph, v, visited)

    # Схлопываем одинаковые минимумы
    print(f"Схлопываем одинаковые минимумы")
    res_vertexes = []
    for p in vertexes:
        print(p)
        if not visited[p]:
            res_vertexes.append(p)
            dfs_join(graph, p, visited)
    print(f"res_vertexes: {res_vertexes}")

    return len(res_vertexes)




    for p1 in vertexes:
        print(f"p1: {p1}, res_vertexes:{res_vertexes}")
        x1, y1 = p1
        uniq = True
        for p2 in res_vertexes:
            x2,y2 = p2
            if (abs(x1-x2) + abs(y1-y2)) == 1:
                uniq = False
                break
        if uniq:
            res_vertexes.append(p1)
    print(f"res_vertexes:{res_vertexes}")
    return ""

    # # assert False
    # def dfs(map_table, graph, vertex, visited, vertexes, is_lt, map_downs):
    #     if vertex not in graph:
    #         return
    #     is_local_minimum = True
    #     for v in graph[vertex]:
    #         if not visited[v]:
    #             visited[v] = True
    #             is_local_minimum = False
    #             # vertexes.append(v)
    #             dfs(map_table, graph, v, visited, vertexes, (is_lt or map_table[v[0]][v[1]] < map_table[vertex[0]][vertex[1]] ), map_downs)
    #     print(f"vertex: {vertex} is_local_minimum: {is_local_minimum} and is_lt:{is_lt} and map_downs[vertex[0]][vertex[1]]: {map_downs[vertex[0]][vertex[1]]}")
    #
    #     if is_local_minimum and is_lt and map_downs[vertex[0]][vertex[1]]:
    #         print(f"is_lt: {is_lt}")
    #         vertexes.append(vertex)
    #
    #
    # vertexes = []
    # copy_visited = visited.copy()
    # for p in graph.keys():
    #     dfs(map_table, graph, p, copy_visited, vertexes, False, map_downs )
    # print(f"vertexes:{ set(vertexes)}")
    #
    # return ""

    assert False

    # for i in range(n):
    #     for j in range(m):
    #         visited[(i, j)] = False
    local_minimum = []
    for i in range(n):
        for j in range(m):
            # minimum = \
            dfs(map_table, (i, j), visited, local_minimum)
            # local_minimum.append(minimum)
    print(f"local_minimum: {local_minimum}")
    print(f"local_minimum: {set(local_minimum)} ({len(set(local_minimum))})")
    count_catch = 0
    return count_catch


def main():
    # считываем входные данные
    n, m, map_table = load_data(INPUT_FILE)
    # Посчет минимального кол-ва ловушек
    count_catch = calc_catch(n, m, map_table)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_catch))


if __name__ == "__main__":
    main()
