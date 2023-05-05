# https://contest.yandex.ru/contest/45468/problems/30/
# Дивизион  B
# 30. НОП с восстановлением ответа
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        n_sequence = list(map(int, file.readline().split()))
        m = int(file.readline())
        m_sequence = list(map(int, file.readline().split()))
    return n, n_sequence, m, m_sequence


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск наибольшей общей подпоследовательности
def find_equal_sub_sequence(n, n_sequence, m, m_sequence):
    '''
    входные данные
    :n — длина первой последовательности
    :n_sequence —  первая последовательность
    :m — длина второй последовательности
    :m_sequence — вторая последовательность

    выходные данные
    :sub_sequence - наибольшая общая подпоследовательность
    '''
    if n == 0 or m == 0:
        return ""
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dict_pathes = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if n_sequence[i - 1] == m_sequence[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] in dict_pathes:
                    dict_pathes[dp[i][j]].append((i, j))
                else:
                    dict_pathes[dp[i][j]] = [(i, j)]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j ], dp[i ][j - 1])
    if len(dict_pathes.keys()) == 0:
        return ""
    sub_sequence = []
    path_keys = sorted(dict_pathes.keys(), reverse=True)
    last = dict_pathes[path_keys[0]][0]
    sub_sequence.append(n_sequence[last[0] - 1])
    for key in path_keys[1:]:
        select_item = None
        for x, y in dict_pathes[key]:
            if x < last[0] and y < last[1]:
                if select_item is None or (x > select_item[0] or y > select_item[1]):
                    select_item = (x, y)
        if select_item is not None:
            sub_sequence.append(n_sequence[select_item[0]- 1] )
            last = select_item
    sub_sequence.reverse()
    return " ".join(map(str, sub_sequence))


def main():
    # считываем входные данные
    n, n_sequence, m, m_sequence = load_data(INPUT_FILE)
    # Поиск наибольшей общей подпоследовательности
    sub_sequence = find_equal_sub_sequence(n, n_sequence, m, m_sequence)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sub_sequence))


if __name__ == "__main__":
    main()
