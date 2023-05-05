# https://contest.yandex.ru/contest/45469/problems/14/
# Дивизион A
# 14. Гистограмма и прямоугольник
PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        hist_string = file.readline().split()
    return int(hist_string[0]), list(map(int, hist_string[1:]))


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет максимальной площади гистрограммы
def calc_square(len_histogram, histogram):
    '''
    входные данные
    :len_histogram - кол-во элементов гистрограммы
    :histogram — входная гистрограмма

    выходные данные
    :max_square - Максимальная площадь прямоугольника из гистрограммы
    '''
    # Ищем в гистрограмме минимальное ограничение справа
    right_limit = [-2] * len_histogram
    stack = []
    for idx in range(len_histogram):
        col = histogram[idx]
        if len(stack) > 0:
            i_stack = len(stack) - 1
            while i_stack >= 0:
                if col < stack[i_stack][0]:
                    right_limit[stack[i_stack][1]] = idx
                    stack.pop()
                else:
                    break
                i_stack -= 1
        stack.append([col, idx])
    for stack_item in stack:
        right_limit[stack_item[1]] = len_histogram

    # Ищем в гистрограмме минимальное ограничение слева
    left_limit = [-2] * len_histogram
    stack = []
    for idx in range(len_histogram - 1, -1, -1):
        col = histogram[idx]
        if len(stack) > 0:
            i_stack = len(stack) - 1
            while i_stack >= 0:
                if col < stack[i_stack][0]:
                    left_limit[stack[i_stack][1]] = idx
                    stack.pop()
                else:
                    break
                i_stack -= 1
        stack.append([col, idx])
    for stack_item in stack:
        left_limit[stack_item[1]] = -1

    # Вычисляем максимальную площадь
    max_square = 0
    for idx in range(len_histogram):
        col = histogram[idx]
        delta = right_limit[idx] - left_limit[idx] - 1
        square = delta * col
        if square > max_square:
            max_square = square
    return max_square


def main():
    # считываем входные данные
    len_histogram, histogram = load_data(INPUT_FILE)
    # Расчет максимальной площади гистрограммы
    max_square = calc_square(len_histogram, histogram)
    # print(f"max_square:{max_square}")
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(max_square))


if __name__ == "__main__":
    main()
