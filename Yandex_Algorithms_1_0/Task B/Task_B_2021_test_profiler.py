# https://contest.yandex.ru/contest/27393/problems/B/
# B. Треугольник
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        a = file.readline()
        b = file.readline()
        c = file.readline()
    return [int(a), int(b), int(c)]


# Записываем результат в output.txt
def save_output(filename, is_available):
    with open(filename, "w") as file:
        if is_available:
            file.write("YES")
        else:
            file.write("NO")


# Определяем возможность построения треугольника с заданными сторонами
def calc_available(edges):
    if min(edges) <= 0:
        return False
    is_available = (edges[0] < edges[1] + edges[2]) and (edges[1] < edges[0] + edges[2]) and (
                edges[2] < edges[0] + edges[1])
    return is_available


def main():
    # считываем входные данные
    edges = load_data(INPUT_FILE)
    # Определяем возможность построения треугольника с заданными сторонами
    is_available = calc_available(edges)
    # # Записываем результат в output.txt
    save_output(OUTPUT_FILE, is_available)


import pytest


@pytest.mark.parametrize(
    "edges, is_available_target",
    [
        ([3, 4, 5], True),
        ([3, 5, 4], True),
        ([5, 4, 3], True),
        ([5, 3, 4], True),
        ([4, 5, 3], True),
        ([4, 3, 5], True),
        ([4, 2, 5], True),
        ([1, 2, 5], False),
        ([1, 1, 7], False),
        ([-3, -4, -5], False),
        ([0, 0, 0], False),
        ([1, 1, 1], True),
        ([0, 3, 5], False),

    ]
)
def test_count_combination_queens(edges, is_available_target):
    is_available = calc_available(edges)
    assert is_available == is_available_target


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    from line_profiler import LineProfiler

    lp = LineProfiler()
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()
