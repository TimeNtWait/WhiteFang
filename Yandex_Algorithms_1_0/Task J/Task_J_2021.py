# https://contest.yandex.ru/contest/27393/problems/J/
# J. Система линейных уравнений - 2
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    numbers = []
    with open(filename, "r") as file:
        for _ in range(6):  # В тесте 1 1 J 24 встретились неверно поданные данные, когда подаются пустые строки
            line = file.readline()
            numbers.append(float(line.strip()))
    return numbers


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Решение уравнения
def calc_equation(a, b, c, d, e, f):
    '''
    входные данные
    :a, b, c, d, e, f - значения уравнения

    выходные данные
    :solution - решение уровнения
    '''
    # a * x + b * y = e
    # c * x + d * y = f

    if (a == 0 and b == 0 and e != 0) or (c == 0 and d == 0 and f != 0):
        return [0]
    x = None
    y = None
    if a == 0 and b != 0:
        y = e / b
    if c == 0 and d != 0:
        if y is None:
            y = f / d
        elif y != f / d:
            return [0]
    if a == 0 and b == 0 and c == 0 and d == 0:
        if e == 0 and f == 0:
            return [5]
        elif e != 0 or f != 0:
            return [0]
    if b == 0 and a != 0:
        x = e / a
    if d == 0 and c != 0:
        if x is None:
            x = f / c
        elif x != f / c:
            return [0]
    if (x is not None) and (y is not None):
        return [2, round(x, 5), round(y, 5)]
    elif x is not None:
        if b != 0:
            y = (e - a * x) / b
        elif d != 0:
            y = (f - c * x) / d
        if y is not None:
            return [2, round(x, 5), round(y, 5)]
        else:
            return [3, round(x, 5)]
    elif y is not None:
        if a != 0:
            x = (e - b * y) / a
        elif c != 0:
            x = (f - d * y) / c
        if x is not None:
            return [2, round(x, 5), round(y, 5)]
        else:
            return [4, round(y, 5)]
    # 1-ое уровнение
    # a * x + b * y = e
    # c * x + d * y = f
    # a * x + b * y = e
    # -a * x + d * y * (-a / c) = f * (-a / c)
    # b * y + d * y * (-a / c) = f * (-a / c) + e
    # y * (b + d * (-a / c)) = f * (-a / c) + e

    # 2 - ое уровнение
    # a * x + b * y = e
    # c * x + d * y = f
    # -c *x + b * y * (-c / a) = e * (-c / a)
    # c * x + d * y = f
    # b * y * (-c / a) + d * y = e * (-c / a) + f
    # y * (b *  (-c / a) + d)  = e * (-c / a) + f
    correct_k = None
    correct_k_2 = None
    if a != 0:
        correct_k = -c / a
        if round(d + b * correct_k, 5) == 0:
            k_solution = (-a / b)
            b_solution = e / b
            k_solution = round(k_solution, 5)
            b_solution = round(b_solution, 5)
        else:
            y1 = (f + e * correct_k) / (d + b * correct_k)
            x1 = (e - b * y1) / a
            x1 = round(x1, 5)
            y1 = round(y1, 5)

    if c != 0:
        correct_k_2 = -a / c
        if round(b + d * correct_k_2, 5) == 0:
            k_solution_2 = (-c / d)
            b_solution_2 = f / d
            k_solution_2 = round(k_solution_2, 5)
            b_solution_2 = round(b_solution_2, 5)
        else:
            y2 = (e + f * correct_k_2) / (b + d * correct_k_2)
            x2 = (f - d * y2) / c
            x2 = round(x2, 5)
            y2 = round(y2, 5)

    if correct_k is not None and correct_k_2 is not None:
        if round(d + b * correct_k, 5) == 0 or round(b + d * correct_k_2, 5) == 0:
            if k_solution == k_solution_2 and b_solution_2 == b_solution:
                return [1, k_solution, b_solution]
            else:
                return [0]
        else:
            if x1 == x2 and y1 == y2:
                return [2, x1, y1]
            else:
                return [0]
    elif correct_k is not None:
        if round(d + b * correct_k, 5) == 0:
            return [1, k_solution, b_solution]
        else:
            return [2, x1, y1]
    elif correct_k_2 is not None:
        if round(b + d * correct_k_2, 5) == 0:
            return [1, k_solution_2, b_solution_2]
        else:
            return [2, x2, y2]
    else:
        return [0]


def main():
    # считываем входные данные
    a, b, c, d, e, f = load_data(INPUT_FILE)
    # Решение уравнения
    solution = calc_equation(a, b, c, d, e, f)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, solution)))


if __name__ == "__main__":
    main()
