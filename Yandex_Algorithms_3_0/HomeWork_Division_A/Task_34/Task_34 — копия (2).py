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
    if (x , y-1) not in visited:
        visited[(x , y-1)] = False
    if (x, y+1) not in visited:
        visited[(x , y+1)] = False

    if x > 0 and map_table[x - 1][y] <= map_table[x][y] and not visited[(x - 1, y)]:
        open_cells.append((x - 1, y))

    if x + 1 < n and map_table[x + 1][y] <= map_table[x][y] and not visited[(x + 1, y)]:
        open_cells.append((x + 1, y))

    if y > 0 and map_table[x][y - 1] <= map_table[x][y] and not visited[(x, y -1)]:
        open_cells.append((x, y - 1))
    if y + 1 < m and map_table[x][y + 1] <= map_table[x][y] and not visited[(x, y+1)]:
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
    if len(open_cells) == 0 :
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

    if n == 0 or m == 0:
        return "0"



    visited = {}
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
