# https://contest.yandex.ru/contest/45468/problems/26/
# Дивизион  B
# 26. Самый дешевый путь
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m = list(map(int, file.readline().split()))
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
    return n, m, matrix


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет минимального штрафа за путь
def calc_min_path(n, m, matrix):
    '''
    входные данные
    :n, m — размер матрицы
    :matrix — матрица штрафов для поиска пути

    выходные данные
    :min_cost - Минимальный вес еды в килограммах, отдав которую можно попасть в правый нижний угол
    '''
    dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = matrix[0][0]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i + 1][j] + matrix[i][j], dp[i][j + 1] + matrix[i][j])
    min_cost = dp[-1][-1]
    return min_cost


def main():
    # считываем входные данные
    n, m, matrix = load_data(INPUT_FILE)
    # Расчет минимального штрафа за путь
    min_cost = calc_min_path(n, m, matrix)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_cost))


if __name__ == "__main__":
    main()
