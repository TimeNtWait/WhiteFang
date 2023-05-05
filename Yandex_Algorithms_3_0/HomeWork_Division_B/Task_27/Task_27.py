# https://contest.yandex.ru/contest/45468/problems/27/
# Дивизион  B
# 27. Вывести маршрут максимальной стоимости
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


# Расчет максимальной стоимости пути
def calc_max_path(n, m, matrix):
    '''
    входные данные
    :n, m — размер матрицы
    :matrix — матрица стоимости для поиска пути

    выходные данные
    :return - Первая строка выходных данных содержит максимальную возможную сумму, вторая — маршрут
    '''
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp_path = [[0] * (m) for _ in range(n)]
    dp[1][1] = matrix[0][0]
    for i in range(n):
        for j in range(m):
            if dp[i + 1][j] > dp[i][j + 1]:
                dp[i + 1][j + 1] = dp[i + 1][j] + matrix[i][j]
                dp_path[i][j] = "R"
            else:
                dp[i + 1][j + 1] = dp[i][j + 1] + matrix[i][j]
                dp_path[i][j] = "D"
    path = []
    while n > 0 and m > 0:
        path.append(dp_path[n - 1][m - 1])
        if dp_path[n - 1][m - 1] == "D":
            n -= 1
        else:
            m -= 1
    max_cost = dp[-1][-1]
    return str(max_cost) + "\n" + " ".join(reversed(path[:-1]))


def main():
    # считываем входные данные
    n, m, matrix = load_data(INPUT_FILE)
    # Расчет максимальной стоимости пути
    max_cost = calc_max_path(n, m, matrix)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(max_cost))


if __name__ == "__main__":
    main()
