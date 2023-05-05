# https://contest.yandex.ru/contest/45469/problems/29/
# Дивизион A
# 29. Движение по полосам
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        m, n = map(int, file.readline().split())
    return m, n


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет кол-ва возможных знаков
def calc_sign(m, n):
    '''
    входные данные
    :m - кол-во различных направлениях
    :n - кол-во полос

    выходные данные
    :count_sign - количество возможных знаков
    '''
    matrix = [[0] * m for i in range(n)]
    for i in range(n):
        matrix[i][0] = 1
    for j in range(m):
        matrix[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i][j - 1]
    count_sign = matrix[-1][-1]
    return count_sign


def main():
    # считываем входные данные
    m, n = load_data(INPUT_FILE)
    # Расчет кол-ва возможных знаков
    count_sign = calc_sign(m, n)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_sign))


if __name__ == "__main__":
    main()
