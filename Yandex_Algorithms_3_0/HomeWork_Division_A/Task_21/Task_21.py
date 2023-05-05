# https://contest.yandex.ru/contest/45469/problems/21/
# Дивизион А
# 21. Разложение в сумму кубов
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


# Разложение в сумму кубов
def calc_sum_cube(n):
    '''
    входные данные
    :n — number

    выходные данные
    :count_cubes - кол-во слогаемых в сумме кубов чтобы получить заданное число
    '''
    numbers = [i for i in range(n + 1)]
    cubes = []
    for i in range(2, n):
        calc_cube = i ** 3
        if calc_cube > n:
            break
        cubes.append(calc_cube)
        numbers[calc_cube] = 1
    if len(cubes) == 0 or n < cubes[0] + 1:
        return numbers[n]

    for number in range(cubes[0] + 1, n + 1):
        calc_min = numbers[number]
        for cube in cubes:
            if cube > number:
                break
            if calc_min > numbers[number - cube] + 1:
                calc_min = numbers[number - cube] + 1
        numbers[number] = calc_min
    return numbers[n]


def main():
    # считываем входные данные
    n = load_data(INPUT_FILE)
    # Разложение в сумму кубов
    count_cubes = calc_sum_cube(n)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_cubes))


if __name__ == "__main__":
    main()
