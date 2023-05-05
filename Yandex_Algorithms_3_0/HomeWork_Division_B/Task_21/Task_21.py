# https://contest.yandex.ru/contest/45468/problems/21/
# Дивизион  B
# 21. Три единицы подряд
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


# Три единицы подряд
def calc_max_not_ones(n):
    '''
    входные данные
    :n — number

    выходные данные
    :count_seq - кол-во последовательностей из нулей и единиц длины N, в которых никакие три единицы не стоят рядом.
    '''
    # База для динамического программирования
    if n < 3:
        return 2 ** n
    dp = [0, 0, 0, 1]
    ones_delta = []
    for i in range(1, len(dp)):
        ones_delta.append(dp[i] - 2 * dp[i - 1])

    # Считаем сколько единиц всего может быть
    for i in range(len(dp), n + 1):
        dp_item = 2 * dp[i - 1] + sum(ones_delta[i - 4:])
        dp.append(dp_item)
        ones_delta.append(dp[i] - 2 * dp[i - 1])
    # В ответ вычитаем из общего кол-ва чисел кол-во чисел с тремя подряд единицами
    count_seq = 2 ** n - dp[-1]
    return count_seq


def main():
    # считываем входные данные
    n = load_data(INPUT_FILE)
    # Три единицы подряд
    count_seq = calc_max_not_ones(n)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_seq))


if __name__ == "__main__":
    main()
