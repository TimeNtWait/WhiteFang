# https://contest.yandex.ru/contest/45469/problems/25/
# Дивизион А
# 25. Увлекательная игра
import math
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, a, b = map(int, file.readline().split())
    return n, a, b


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Увлекательная игра
def calc_nice_game(n, a, b):
    '''
    входные данные
    :n — кол-во уровней треугольника
    :a - кол-во отдаваемых конфет, в случае ответа «да»
    :b - кол-во отдаваемых конфет, а в случае ответа «нет»

    выходные данные
    :min_candies - Минимальное требуемое количество конфет
    '''
    if n == 1:
        return 0
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a == 0 and b == 0:
        return 0

    dp = [0]*(n+1)
    for i in range(1, n+1):
        max_costes = []
        for k in range(1, i):
            max_numb = max(dp[k]+a, dp[i-k]+ b)
            max_costes.append(max_numb)
        if len(max_costes) > 0:
            dp[i] = min(max_costes)
    min_candies = dp[-1]
    # print(f"min_candies: {min_candies}")
    return min_candies


import pytest


@pytest.mark.parametrize(
    "n, a, b, target_sum",
    [
        (14, 2, 2, 8),
        (11, 1, 1, 4),
        (8, 1, 1, 3),
        (10, 4, 2, 12),
        (6, 1, 2, 4),
        (11, 3, 4, 14),
        (3, 10, 10, 20),
        (930, 1, 10, 43), # 44
        (931, 1, 10, 44), # 45
        (966, 3, 10, 63), # 46
        (967, 3, 10, 64), # 47
        (993, 13, 919181, 932064),# 48
    ]
)

def test_nice_game(n, a, b, target_sum):
    min_candies = calc_nice_game(n, a, b)
    print(f"min_candies: {min_candies}, target_sum:{target_sum}")
    assert min_candies == target_sum

def main():
    # считываем входные данные
    n, a, b = load_data(INPUT_FILE)
    # Увлекательная игра
    min_candies = calc_nice_game(n, a, b)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_candies))


if __name__ == "__main__":
    # main()
    pytest.main(args=[__file__])
