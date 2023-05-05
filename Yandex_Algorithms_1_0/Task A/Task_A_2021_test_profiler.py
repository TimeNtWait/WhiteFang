# https://contest.yandex.ru/contest/27393/problems/A/
# A. Кондиционер
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"
modes = {"fan": 0, "heat": 1, "freeze": 2, "auto": 3, }


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        troom, tcond = file.readline().split()
        type_mode = file.readline().strip()
    return int(troom), int(tcond), type_mode


# Записываем результат в output.txt
def save_output(filename, data):
    with open(filename, "w") as file:
        file.write(data)


# Рассчитываем новую температуру
def calc_troom(troom, tcond, mode):
    if mode == 1:
        return max(troom, tcond)
    elif mode == 2:
        return min(troom, tcond)
    elif mode == 3:
        return tcond
    return troom


def main():

    # считываем входные данные
    troom, tcond, type_mode = load_data(INPUT_FILE)
    # рассчитываем температуру
    new_troom = calc_troom(troom, tcond, modes[type_mode])
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(new_troom))


import pytest


@pytest.mark.parametrize(
    "troom, tcond, type_mode, new_troom",
    [
        (10, 20, "heat", 20),
        (20, 10, "heat", 20),
        (-50, 50, "heat", 50),
        (-50, -49, "heat", -49),
        (50, 49, "heat", 50),
        (10, 10, "heat", 10),

        (10, 20, "freeze", 10),
        (20, 10, "freeze", 10),
        (-50, 50, "freeze", -50),
        (-50, -49, "freeze", -50),
        (50, 49, "freeze", 49),
        (10, 10, "freeze", 10),

        (10, 20, "fan", 10),
        (20, 10, "fan", 20),
        (-50, 50, "fan", -50),
        (-50, -49, "fan", -50),
        (50, 49, "fan", 50),
        (10, 10, "fan", 10),

        (10, 20, "auto", 20),
        (20, 10, "auto", 10),
        (-50, 50, "auto", 50),
        (-50, -49, "auto", -49),
        (50, 49, "auto", 49),
        (10, 10, "auto", 10),
    ]
)
def test_count_combination_queens(troom, tcond, type_mode, new_troom):
    res_troom = calc_troom(troom, tcond, modes[type_mode])
    assert res_troom == new_troom


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    from line_profiler import LineProfiler
    lp = LineProfiler()
    lp_wrapper = lp(main)
    lp_wrapper()
    lp.print_stats()
