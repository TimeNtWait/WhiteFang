# https://contest.yandex.ru/contest/27393/problems/I/
# I. Узник замка Иф
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


# Расчет сторон кирпичей
def calc_side_block(a, b, c, d, e):
    '''
    входные данные
    :a - сторона 1 убираемого блока
    :b - сторона 1 убираемого блока
    :с - сторона 3 убираемого блока
    :d - сторона 1 отверстия
    :e - сторона 2 отверстия

    выходные данные
    :is_drop_block - минимальное и максимальное время ожидания
    '''
    block_sizes = [sorted([a, b]), sorted([a, c]), sorted([b, c])]
    hole_size = sorted([d, e])
    is_drop_block = "NO"
    for side in block_sizes:
        if (hole_size[0] - side[0]) >= 0 and (hole_size[1] - side[1]) >= 0:
            is_drop_block = "YES"
            break
    return is_drop_block


def main():
    # считываем входные данные
    a, b, c, d, e = load_data(INPUT_FILE)
    # Расчет сторон кирпичей
    is_drop_block = calc_side_block(a, b, c, d, e)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, is_drop_block)


import pytest


@pytest.mark.parametrize(
    "numbers, target_result",
    [
        ([1, 1, 1, 1, 1, ], "YES"),
        ([2, 2, 2, 1, 1, ], "NO"),
        ([1, 1, 2, 1, 1, ], "YES"),

    ]
)
def test_calc_side_block(numbers, target_result):
    result = calc_side_block(*numbers)
    assert result == target_result


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(main)
    # lp_wrapper()
    # lp.print_stats()
