# https://contest.yandex.ru/contest/45469/problems/30/
# Дивизион A
# 30. Распил брусьев
import math
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        l, n = map(int, file.readline().split())
        splites = list(map(int, file.readline().split()))
    return l, n, splites


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет минимальной стоимости распила
def calc_min_price(l, n, splites):
    '''
    входные данные
    :l - длину бруса
    :n -  количество распилов

    выходные данные
    :min_price - количество возможных знаков
    '''
    print(l, n, splites)
    # расширяем места распила граничными значениями
    splites = [0] + splites + [l]
    n += 2
    dp = [[math.inf] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
        if i < n- 1:
            dp[i][i+1] = 0

    for dgnl in range(2,n):
        print(f"dgnl:{dgnl}")
        for i in range(n-dgnl):
            cost = splites[i+dgnl] - splites[i]
            print(f"i:{i} cost:{cost}")
            for j in range(1, dgnl):
                dp[i][i + dgnl] = min(dp[i][i + dgnl], dp[i][i + j] + dp[i + j][i + dgnl])
            dp[i][i + dgnl] += cost

    for i in range(n):
        print(dp[i])

    min_price = 0
    return min_price


    # dp[i][j] = max(A[i] * A[k] * A[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
    i = 2
    j = 3
    max(i+j for k in range(i, j*5))
    [[k+j] for k in range(1, 10)]
    print([[k+j] for k in range(i, j*5)])
    print(max(i+j for k in range(i, j*5)))
    min_price = 0
    return min_price

    # matrix = [[0] * m for i in range(n)]
    # for i in range(n):
    #     matrix[i][0] = 1
    # for j in range(m):
    #     matrix[0][j] = 1
    #
    # for i in range(1, n):
    #     for j in range(1, m):
    #         matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i][j - 1]
    # count_sign = matrix[-1][-1]
    # return count_sign


def main():
    # считываем входные данные
    l, n, splites = load_data(INPUT_FILE)
    # Расчет минимальной стоимости распила
    min_price = calc_min_price(l, n, splites)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_price))


if __name__ == "__main__":
    main()
