# https://contest.yandex.ru/contest/45468/problems/25/
# Дивизион  B
# 25. Гвоздики
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        nails = list(map(int, file.readline().split()))
    return n, nails


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Минимальная суммарная длина нитки для гвоздиков
def calc_thread_nails(n, nails):

    '''
    входные данные
    :n — кол-во гвоздей
    :nails - координаты гвоздей

    выходные данные
    :min_thread_nails - Минимальная суммарная длина нитки для гвоздиков
    '''
    nails = sorted(nails)
    print((n, nails))
    # База для динамического программирования
    min_thread_nails = [0] * (n )
    delta_nails = [0]
    for i in range(1, len(nails)):
        delta_nails.append(nails[i] - nails[i-1])
    min_thread_nails[1] = delta_nails[1]
    min_thread_nails[2] = min_thread_nails[1] + (delta_nails[2])

    for i in range(3, n):
        min_thread_nails[i] = min(min_thread_nails[i-1], min_thread_nails[i-2]) + delta_nails[i]
    return min_thread_nails[-1]


def main():
    # считываем входные данные
    n, nails = load_data(INPUT_FILE)
    # Суммарная длина нитки для гвоздиков
    thread_nails = calc_thread_nails(n, nails)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(thread_nails))


if __name__ == "__main__":
    main()
