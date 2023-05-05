# https://contest.yandex.ru/contest/45469/problems/22/
# Дивизион А
# 22. НВП с восстановлением ответа
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        sequence = list(map(int, file.readline().split()))
    return n, sequence


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# НВП с восстановлением ответа
def calc_max_sub_sequence(n, sequence):

    '''
    входные данные
    :n — кол-во чисел
    :sequence — последовательнось чисел

    выходные данные
    :sub_sequence - НВП с восстановлением ответа
    '''
    dp = [1]*(n)
    dp_path = [-1]*(n)
    for i in range(1, n):
        numb = sequence[i]
        for j in range(i-1, -1, -1):
            pre_numb = sequence[j]
            if numb > pre_numb:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    dp_path[i] = j
    find_index = dp.index(max(dp))
    path = [sequence[find_index]]
    # Восставновление пути
    while dp_path[find_index] > -1:
        find_index = dp_path[find_index]
        path.append(sequence[find_index])
    return reversed(path)


def main():
    # считываем входные данные
    n, sequence = load_data(INPUT_FILE)
    # НВП с восстановлением ответа
    sub_sequence = calc_max_sub_sequence(n, sequence)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, " ".join(map(str, sub_sequence)))


if __name__ == "__main__":
    main()
