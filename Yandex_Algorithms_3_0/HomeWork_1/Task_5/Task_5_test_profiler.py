# https://contest.yandex.ru/contest/45468/problems/5/
# 5. Хорошая строка

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    n_rows = 0
    letters = []
    with open(filename, "r") as file:
        n_rows = int(file.readline())
        for _ in range(n_rows):
            letters.append(int(file.readline()))
    return n_rows, letters


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определяем уровень хорошести строк
def calc_goodness_string(n_rows, letters):
    '''
    входные данные
    :n_rows - кол-во рассматриваемых букв
    :letters - массив кол-ва встречаемости для каждой буквы

    выходные данные
    :goodness_level - уровень хорошести строк
    '''
    # print(n_rows, letters)
    if n_rows <= 1:
        return 0
    goodness_level = 0
    for idx in range(len(letters) - 1):
        goodness_level += min(letters[idx + 1], letters[idx])
    print(f"goodness_level: {goodness_level}")
    return goodness_level


def main():
    # считываем входные данные
    n_rows, letters = load_data(INPUT_FILE)
    # Определяем уровень хорошести строк
    goodness_level = calc_goodness_string(n_rows, letters)
    # print(f"goodness_level: {goodness_level}")
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(goodness_level))


import pytest


@pytest.mark.parametrize(
    "numbers, target_goodness_level",
    [
        ([1, 1], 0),
        ([1, 100], 0),
        ([3, 1, 1, 1, ], 2),
        ([3, 1, 2, 1, ], 2),
        ([3, 2, 2, 1, ], 3),
        ([2, 3, 4, ], 3),
        ([2, 34, 58, ], 34),
        ([26, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ], 25),
        ([6, 9, 62, 38, 35, 1, 95], 84),
    ]
)
def test_calc_goodness_string(numbers, target_goodness_level):
    goodness_level = calc_goodness_string(numbers[0], numbers[1:])
    print(f"goodness_level: {goodness_level}, target_goodness_level:{target_goodness_level}")
    assert goodness_level == target_goodness_level


if __name__ == "__main__":
    main()
    # pytest.main(args=[__file__])
    from random import randint
    # n = 10000
    # diego_stickers = [randint(1, 10 ** 9) for _ in range(n)]
    # count_guests =10000
    # limits_sticker_guests = [randint(1, 10 ** 9) for _ in range(count_guests)]
    #
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_stickers)
    # lp_wrapper(n, diego_stickers, count_guests, limits_sticker_guests)
    # lp.print_stats()
