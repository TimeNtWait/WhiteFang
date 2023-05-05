# https://contest.yandex.ru/contest/27393/problems/F/
# F. Расстановка ноутбуков
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    numbers = []
    with open(filename, "r") as file:
        numbers = map(int, file.readline().split())
    return numbers


# # Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определеляем оптимальное расположение ноутбуков
def calc_size_table(a1, b1, a2, b2):
    '''
    входные данные
    :a1 - сторона a ноутбука 1
    :b1 - сторона b ноутбука 1
    :a2 - сторона a ноутбука 2
    :b2 - сторона b ноутбука 2

    выходные данные
    :c - сторона c стола
    :d - сторона d стола
    '''

    # Варианты расположения ноутбуков
    sides = [
        # последовательное расположение
        ((a1 + a2), (b1 + b2)),
        ((a1 + b2), (b1 + a2)),
        # параллельное расположение
        (max(a1, a2), (b1 + b2)),
        (max(a1, b2), (b1 + a2)),
        (max(b1, b2), (a1 + a2)),
        (max(b1, a2), (a1 + b2)),
    ]
    # Определяем начальные значения минимальной площади
    min_side = sides[0]
    min_s = min_side[0] * min_side[1]
    for v in sides:
        s = v[0] * v[1]
        if s < min_s:
            min_side = v
            min_s = s
    return min_side


def main():
    # считываем входные данные
    a1, b1, a2, b2 = load_data(INPUT_FILE)
    # Определеляем оптимальное расположение ноутбуков
    c, d = calc_size_table(a1, b1, a2, b2)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, f"{c} {d}")


if __name__ == "__main__":
    main()
