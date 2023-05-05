# https://contest.yandex.ru/contest/27393/problems/A/
# A. Кондиционер
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


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
    modes = {"fan": 0, "heat": 1, "freeze": 2, "auto": 3, }
    # считываем входные данные
    troom, tcond, type_mode = load_data(INPUT_FILE)
    # рассчитываем температуру
    new_troom = calc_troom(troom, tcond, modes[type_mode])
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(new_troom))


if __name__ == "__main__":
    main()
