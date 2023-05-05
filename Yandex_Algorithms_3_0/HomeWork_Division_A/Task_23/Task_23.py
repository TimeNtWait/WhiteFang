# https://contest.yandex.ru/contest/45469/problems/23/
# Дивизион А
# 23. Количество треугольников
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
    return n


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Количество треугольников
def calc_triangles(n):
    '''
    входные данные
    :n — кол-во уровней треугольника

    выходные данные
    :count_triangles - Количество треугольников
    '''
    if n % 2 == 0:
        count_triangles = (n * (n + 2) * (2 * n + 1)) / 8
    else:
        count_triangles = (n * (n + 2) * (2 * n + 1) - 1) / 8
    return int(count_triangles)


def main():
    # считываем входные данные
    n = load_data(INPUT_FILE)
    # Количество треугольников
    count_triangles = calc_triangles(n)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_triangles))


if __name__ == "__main__":
    main()
