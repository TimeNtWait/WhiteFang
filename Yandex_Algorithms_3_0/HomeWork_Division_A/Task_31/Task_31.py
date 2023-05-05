# https://contest.yandex.ru/contest/45469/problems/31/
# Дивизион A
# 31. Площадь комнаты
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        map_table = []
        for _ in range(n):
            row = file.readline().strip()
            # оцифровываем карту лабиринта
            row = row.replace(".", "0")
            row = row.replace("*", "1")
            map_table.append(list(map(int, row)))
        center = tuple(map(int, file.readline().split()))
    return n, map_table, center


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


def get_open_cells(map_table, point):
    n = len(map_table)
    open_cells = []
    x, y = point
    if x > 0 and map_table[x - 1][y] == 0:
        open_cells.append((x - 1, y))

    if x + 1 < n and map_table[x + 1][y] == 0:
        open_cells.append((x + 1, y))

    if y > 0 and map_table[x][y - 1] == 0:
        open_cells.append((x, y - 1))

    if y + 1 < n and map_table[x][y + 1] == 0:
        open_cells.append((x, y + 1))

    return open_cells


def dfs(map_table, graph, point, visited):
    open_cells = get_open_cells(map_table, point)
    for p in open_cells:
        if p not in visited:
            visited[p] = False
    graph[point] = open_cells
    for v in graph[point]:
        if not visited[v]:
            visited[v] = True
            dfs(map_table, graph, v, visited)


# Расчет площади комнаты
def calc_square_room(n, map_table, center):
    '''
    входные данные
    :n — размер лабиринта
    :map_table — матрица лабиринта, где "." (0) - пустая ячейка и "*" (1) - стена
    :center — начальная координата, от которой считается размер площади

    выходные данные
    :square_room – количество пустых клеток в данной комнате.
    '''
    if n == 0:
        return "0"

    graph = {}
    center = (center[0] - 1, center[1] - 1)
    visited = {center: False}
    dfs(map_table, graph, center, visited)
    square_room = len(visited.keys())
    return square_room


def main():
    # считываем входные данные
    n, map_table, center = load_data(INPUT_FILE)
    # Площадь комнаты
    square_room = calc_square_room(n, map_table, center)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(square_room))


if __name__ == "__main__":
    main()
