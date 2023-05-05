# https://contest.yandex.ru/contest/45468/problems/39/
# Дивизион  B
# 39. Путь спелеолога
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        cube_area = []
        for _ in range(n):
            file.readline()
            matrix = []
            for _ in range(n):
                row = file.readline().strip()
                # оцифровываем карту
                row = row.replace(".", "0")
                row = row.replace("#", "2")
                row = row.replace("S", "1")
                matrix.append(list(map(int, row)))
            cube_area.append(matrix)
    return n, cube_area


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск выхода
def find_path(n, cube_area):
    '''
    входные данные
    :n - измерение кубического пространства, размер каждого из трех измерений
    :cube_area - трехмерный массив лабиринта, где "." (0) - пустая ячейка и "#" (2) - стена, и "S" (1) - старт

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    start = None
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cube_area[i][j][k] == 2:
                    cube_area[i][j][k] = -1
                if cube_area[i][j][k] == 1:
                    start = (i, j, k)
                    cube_area[i][j][k] = 0
    queue_bfs = deque()
    queue_bfs.append(start)
    steps = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), ]
    length_route = 0
    while len(queue_bfs) > 0:
        point = queue_bfs.popleft()
        if point[0] == 0:
            length_route = cube_area[point[0]][point[1]][point[2]]
            break
        for x, y, z in steps:
            new_x = point[0] + x
            new_y = point[1] + y
            new_z = point[2] + z
            if 0 <= new_x < n and 0 <= new_y < n and 0 <= new_z < n:
                if cube_area[new_x][new_y][new_z] == 0:
                    cube_area[new_x][new_y][new_z] = cube_area[point[0]][point[1]][point[2]] + 1
                    queue_bfs.append((new_x, new_y, new_z))
    return length_route


def main():
    # считываем входные данные
    n, cube_area = load_data(INPUT_FILE)
    # Поиск выхода
    length_route = find_path(n, cube_area)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
