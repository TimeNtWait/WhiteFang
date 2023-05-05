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
    # расширяем места распила граничными значениями
    splites = [0] + splites + [l]
    n += 2
    dp = [[math.inf] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0
        if i < n - 1:
            dp[i][i + 1] = 0

    for dgnl in range(2, n):
        for i in range(n - dgnl):
            cost = splites[i + dgnl] - splites[i]
            for j in range(1, dgnl):
                dp[i][i + dgnl] = min(dp[i][i + dgnl], dp[i][i + j] + dp[i + j][i + dgnl])
            dp[i][i + dgnl] += cost
    min_price = dp[0][-1]
    return min_price


def main():
    # считываем входные данные
    l, n, splites = load_data(INPUT_FILE)
    # Расчет минимальной стоимости распила
    min_price = calc_min_price(l, n, splites)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_price))


if __name__ == "__main__":
    main()
