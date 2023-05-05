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


if __name__ == "__main__":
    main()
