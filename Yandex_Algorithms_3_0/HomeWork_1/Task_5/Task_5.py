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
    if n_rows <= 1:
        return 0
    goodness_level = 0
    for idx in range(len(letters) - 1):
        goodness_level += min(letters[idx + 1], letters[idx])
    return goodness_level


def main():
    # считываем входные данные
    n_rows, letters = load_data(INPUT_FILE)
    # Определяем уровень хорошести строк
    goodness_level = calc_goodness_string(n_rows, letters)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(goodness_level))


if __name__ == "__main__":
    main()
