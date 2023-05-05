# https://contest.yandex.ru/contest/45468/problems/4/
# 4. Контрольная работа

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    numbers = []
    with open(filename, "r") as file:
        for _ in range(4):
            numbers.append(int(file.readline()))
    return numbers


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определяем совпадение вариантов на контрольной
def calc_exam(n_students, n_variants, n_row, side):
    '''
    входные данные
    :n_students - количество учеников в классе
    :n_variants - количество подготовленных для контрольной вариантов заданий
    :n_row - номер ряда, на который уже сел Петя
    :side - цифра 1, если он сел на правое место, и 2, если на левое

    выходные данные
    :result_exam - номер ряда, куда следует сесть Васе и номер стороны: 1-правое место, 2-левое место
    '''
    # Если вариантов больше или столько же сколько студентов, тогда нельзя списать
    if n_variants >= n_students:
        return [-1]
    all_rows = (n_students + 1) // 2
    # Развернем все места в линию
    places = (n_row - 1) * 2 + side
    choice_variant = places % n_variants
    # Если разделилось на цело то это максимальный вариант
    if choice_variant == 0:
        choice_variant = n_variants
    # Если выбранный вариант может встретится только один раз, во всем классе, то второй такой варинат уже никак
    if choice_variant * 2 > n_students:
        return [-1]
    forward_select_place = places - n_variants
    backward_select_place = places + n_variants

    forward_row = (forward_select_place + 1) // 2
    forward_side = (forward_select_place - 1) % 2 + 1

    backward_row = (backward_select_place + 1) // 2
    backward_side = (backward_select_place - 1) % 2 + 1

    if (backward_row - n_row) <= (n_row - forward_row) and backward_row <= all_rows and (
            (backward_row - 1) * 2 + backward_side) <= n_students:
        result_exam = [backward_row, backward_side]
    elif forward_row > 0:
        result_exam = [forward_row, forward_side]
    else:
        result_exam = [-1]
    return result_exam


def main():
    # считываем входные данные
    n_students, n_variants, n_row, side = load_data(INPUT_FILE)
    # Определяем совпадение вариантов на контрольной
    result_exam = calc_exam(n_students, n_variants, n_row, side)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, result_exam)))


if __name__ == "__main__":
    main()
