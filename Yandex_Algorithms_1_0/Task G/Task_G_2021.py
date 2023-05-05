# https://contest.yandex.ru/contest/27393/problems/G/
# G. Детали
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


# Определеляем оптимальное кол-во деталей
def calc_count_detail(n, k, m):
    '''
    входные данные
    :n - общая масса материала
    :k - требуемый размер заготовки
    :m - масса итоговой детали

    выходные данные
    :count_detail - кол-во итоговых деталей
    '''
    # Проверяем ошибочные данные
    if m > k:
        return 0
    count_detail = 0
    free_volume = n
    # Идем циклом пока есть материал доступный для изготовления деталей
    while free_volume >= k:
        # Считаем сколько всего деталей можно сделать из свободного материала
        details = int(free_volume / k) * int(k / m)
        # Считаем оставшийся материал
        free_volume -= details * m
        count_detail += details
    return count_detail


def main():
    # считываем входные данные
    n, k, m = load_data(INPUT_FILE)
    # Определеляем оптимальное кол-во деталей
    count_detail = calc_count_detail(n, k, m)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_detail))


if __name__ == "__main__":
    main()
