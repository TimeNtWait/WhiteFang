# https://contest.yandex.ru/contest/27393/problems/H/
# H. Метро

import math

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line.strip()))
    return numbers


# # Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определеляем время движения поездов
def calc_time_train(a, b, n, m):
    '''
    входные данные
    :a - интервал поезда на пути 1
    :b - интервал поезда на пути 2
    :n - кол-во поездов на пути 1
    :m - кол-во поездов на пути 1

    выходные данные
    :min_max_time - минимальное и максимальное время ожидания
    '''

    # Функция рассчета мин макс время
    def min_max_time(interval, n_train):
        # Минимальное время когда поезд находился на платофрме в начале и в конце подсчета
        min_time = n_train + (n_train - 1) * interval
        # Максимальное время когда в начале и в конце учитывается интервал отсутствия поезда
        max_time = n_train + (n_train - 1) * interval + 2 * interval
        return min_time, max_time

    # Определяем мин макс время для каждого пути
    min_time_a, max_time_a = min_max_time(a, n)
    min_time_b, max_time_b = min_max_time(b, m)

    # # Проверяем ошибочность данных
    if max_time_a < min_time_b or max_time_b < min_time_a:
        return [-1]
    # Определяем мин макс время
    # Сортируем данные по времени ожидания для вывода
    min_max_time = sorted([max(min_time_a, min_time_b), min(max_time_a, max_time_b)])
    return min_max_time


def main():
    # считываем входные данные
    a, b, n, m = load_data(INPUT_FILE)
    # Определеляем время движения поездов
    result_min_max_time = calc_time_train(a, b, n, m)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, result_min_max_time)))


import pytest


@pytest.mark.parametrize(
    "numbers, target_min_max_time",
    [
        ([1, 3, 3, 2, ], [5, 7]),
        ([1, 5, 1, 2, ], [-1]),
        # ([3, 2, 7, 11, ], [27, 32]), - не верно
        ([3, 2, 7, 11, ], [31, 31]),
    ]
)
def test_calc_calc_time_train(numbers, target_min_max_time):
    result_min_max_time = calc_time_train(*numbers)
    # print(f"result_min_max_time: {result_min_max_time}, target_min_max_time: {target_min_max_time}")
    assert result_min_max_time == target_min_max_time


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(main)
    # lp_wrapper()
    # lp.print_stats()
