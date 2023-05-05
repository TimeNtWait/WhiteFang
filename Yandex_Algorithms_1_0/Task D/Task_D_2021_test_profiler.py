# https://contest.yandex.ru/contest/27393/problems/D/
# D. Уравнение с корнем

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line))
    return numbers


# # Записываем результат в output.txt
def save_output(filename, solve):
    with open(filename, "w") as file:
        file.write(solve)


# Ищем корни уравнения
def solve_equation(numbers):
    a, b, c = numbers
    if c < 0:
        result_solve = "NO SOLUTION"
    elif a == 0:
        if b == c ** 2:
            result_solve = "MANY SOLUTIONS"
        else:
            result_solve = "NO SOLUTION"
    # elif c ** 2 - b == 0:
    #     result_solve
    # c=2 b=4 4 2
    else:
        x = (c ** 2 - b) / a
        # Проверка, что решения в целых числах
        if int(x) == x:
            result_solve = str(int(x))
        else:
            result_solve = "NO SOLUTION"
    return result_solve


def main():
    # считываем входные данные
    numbers = load_data(INPUT_FILE)
    # Ищем корни уравнения
    solve = solve_equation(numbers)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, solve)


# if __name__ == "__main__":
#     main()

import pytest


@pytest.mark.parametrize(
    "numbers, target_solve",
    [
        ([1, 0, 0, ], 0,),
        ([1, 2, 3, ], 7,),
        ([1, 2, -3, ], "NO SOLUTION",),
        ([0, 0, 0, ], "MANY SOLUTIONS",),
        ([0, 0, 5, ], "NO SOLUTION",),
        ([0, 3, 4, ], "NO SOLUTION",),
        ([5, 0, 1, ], "NO SOLUTION",),
        ([25, 9, 3, ], 0,),
        ([1, 0, 0, ], 0,),

    ]
)
def test_count_combination_queens(numbers, target_solve):
    result_solve = solve_equation(numbers)
    assert result_solve == target_solve


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    from line_profiler import LineProfiler

    lp = LineProfiler()
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()
