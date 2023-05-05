# https://contest.yandex.ru/contest/45469/problems/36/
# Дивизион  A
# 36. Два коня
from collections import deque
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    chess_letters = "abcdefgh"
    with open(filename, "r") as file:
        h1, h2 = file.readline().split()
        h1 = (chess_letters.index(h1[0]), int(h1[1]) - 1)
        h2 = (chess_letters.index(h2[0]), int(h2[1]) - 1)
    return h1, h2


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(h1, h2):
    '''
    входные данные
    :h1 - координаты первого коня
    :h2 - координаты второго коня

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    n = 8
    matrix = [[(math.inf, math.inf)] * n for _ in range(n)]
    matrix[h1[0]][h1[1]] = (0, math.inf)
    matrix[h2[0]][h2[1]] = (math.inf, 0)

    steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    queue_bfs1 = deque()
    queue_bfs1.append(h1)
    while len(queue_bfs1) > 0:
        point = queue_bfs1.popleft()
        for x, y in steps:
            if 0 <= point[0] + x < n and 0 <= point[1] + y < n:
                new_x = point[0] + x
                new_y = point[1] + y
                if matrix[point[0]][point[1]][0] + 1 < matrix[new_x][new_y][0]:
                    matrix[new_x][new_y] = (matrix[point[0]][point[1]][0] + 1, matrix[new_x][new_y][1])
                    queue_bfs1.append((new_x, new_y))

    queue_bfs2 = deque()
    queue_bfs2.append(h2)
    while len(queue_bfs2) > 0:
        point = queue_bfs2.popleft()
        for x, y in steps:
            if 0 <= point[0] + x < n and 0 <= point[1] + y < n:
                new_x = point[0] + x
                new_y = point[1] + y
                if matrix[point[0]][point[1]][1] + 1 < matrix[new_x][new_y][1]:
                    matrix[new_x][new_y] = (matrix[new_x][new_y][0], matrix[point[0]][point[1]][1] + 1)
                    queue_bfs2.append((new_x, new_y))
    min_find = math.inf
    for i in range(n):
        for j in range(n):
            if matrix[i][j][0] == matrix[i][j][1]:
                min_find = min(min_find, matrix[i][j][0])
    if math.isinf(min_find):
        return -1
    else:
        return min_find


def main():
    # считываем входные данные
    h1, h2 = load_data(INPUT_FILE)
    # Поиск минимального пути
    length_route = find_path(h1, h2)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
