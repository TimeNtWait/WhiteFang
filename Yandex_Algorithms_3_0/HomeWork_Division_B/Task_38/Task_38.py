# https://contest.yandex.ru/contest/45468/problems/38/
# Дивизион  B
# 38. Блохи
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m, s, t, q = map(int, file.readline().split())
        fleas = []
        for _ in range(q):
            fleas.append(list(map(int, file.readline().split())))
    return n, m, s, t, q, fleas


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск длины кратчайшего пути
def find_path(n, m, s, t, q, fleas):
    '''
    входные данные
    :n, m  — размер клеточного поля
    :s, t - координаты целевой клетки - кормушки
    :q — кол-во блох
    :fleas - координаты блох

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    if m == 0 or n == 0 or q == 0:
        return -1
    matrix = [[math.inf] * m for _ in range(n)]
    matrix[s - 1][t - 1] = 0
    queue_bfs = set([])
    queue_bfs.add((s - 1, t - 1))
    steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    while len(queue_bfs) > 0:
        point = queue_bfs.pop()
        for x, y in steps:
            if 0 <= point[0] + x < n and 0 <= point[1] + y < m:
                new_x = point[0] + x
                new_y = point[1] + y
                if matrix[point[0]][point[1]] + 1 < matrix[new_x][new_y]:
                    matrix[new_x][new_y] = matrix[point[0]][point[1]] + 1
                    queue_bfs.add((new_x, new_y))

    sum_length_route = 0
    for flea in fleas:
        x = flea[0] - 1
        y = flea[1] - 1
        if math.isinf(matrix[x][y]):
            return -1
        sum_length_route += matrix[x][y]
    return sum_length_route


def main():
    # считываем входные данные
    n, m, s, t, q, fleas = load_data(INPUT_FILE)
    # Поиск длины кратчайшего пути
    length_route = find_path(n, m, s, t, q, fleas)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
