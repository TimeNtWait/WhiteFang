# https://contest.yandex.ru/contest/45469/problems/38/
# Дивизион  A
# 38. Игрушечный лабиринт
import math
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return n, m, matrix


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(n, m, matrix):
    '''
    входные данные
    :n, m - размер поля
    :matrix - матрица поля с указанием расположения препятствий (1) и выходов (2), незанятые ячейки (0)

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                matrix[i][j] = -1
            if matrix[i][j] == 2:
                matrix[i][j] = -2
            if matrix[i][j] == 0:
                matrix[i][j] = math.inf
    matrix[0][0] = 0

    queue_bfs = deque()
    queue_bfs.append((0, 0))

    length_route = math.inf
    while len(queue_bfs) > 0:
        point = queue_bfs.popleft()
        x, y = point
        if matrix[x][y] == -2:
            break
        for dy in range(y, m):
            if dy + 1 == m or matrix[x][dy + 1] == -1:
                if matrix[x][y] + 1 < matrix[x][dy]:
                    matrix[x][dy] = matrix[x][y] + 1
                    queue_bfs.append((x, dy))
                break
            elif matrix[x][dy + 1] == -2:
                length_route = min(length_route, matrix[x][y] + 1)
                queue_bfs.appendleft((x, dy + 1))
                break
        for dy in range(y, -1, -1):
            if dy == 0 or matrix[x][dy - 1] == -1:
                if matrix[x][y] + 1 < matrix[x][dy]:
                    matrix[x][dy] = matrix[x][y] + 1
                    queue_bfs.append((x, dy))
                break
            elif matrix[x][dy - 1] == -2:
                length_route = min(length_route, matrix[x][y] + 1)
                queue_bfs.appendleft((x, dy - 1))
                break

        for dx in range(x, n):
            if dx + 1 == n or matrix[dx + 1][y] == -1:
                if matrix[x][y] + 1 < matrix[dx][y]:
                    matrix[dx][y] = matrix[x][y] + 1
                    queue_bfs.append((dx, y))
                break
            elif matrix[dx + 1][y] == -2:
                length_route = min(length_route, matrix[x][y] + 1)
                queue_bfs.appendleft((dx + 1, y))
                break

        for dx in range(x, -1, -1):
            if dx == 0 or matrix[dx - 1][y] == -1:
                if matrix[x][y] + 1 < matrix[dx][y]:
                    matrix[dx][y] = matrix[x][y] + 1
                    queue_bfs.append((dx, y))
                break
            elif matrix[dx - 1][y] == -2:
                length_route = min(length_route, matrix[x][y] + 1)
                queue_bfs.appendleft((dx - 1, y))
                break
    # print(f"length_route: {length_route}")
    return length_route


def main():
    # считываем входные данные
    n, m, matrix = load_data(INPUT_FILE)
    # Поиск минимального пути
    length_route = find_path(n, m, matrix)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
