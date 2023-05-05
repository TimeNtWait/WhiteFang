# https://contest.yandex.ru/contest/45468/problems/9/
# 9. Сумма в прямоугольнике

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m, k = list(map(int, file.readline().split()))
        matrix = []
        for _ in range(n):
            row = list(map(int, file.readline().split()))
            matrix.append(row)
        requests = []
        for _ in range(k):
            row = list(map(int, file.readline().split()))
            requests.append(row)
    return n, m, k, matrix, requests


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет суммы в прямоугольнике
def calc_sum(n, m, k, matrix, requests):
    '''
    входные данные
    :n, :m — размеры матрицы (1 ≤ N, M ≤ 1000)
    :k -  количество запросо
    :matrix - матрица, заполненая значениями
    :requests - запросы расчета сум

    выходные данные
    :sum_responses - сумма чисел в соответствии с запросом
    '''
    # Так как задача про многое кол-во запросов, то лучше делать через префиксные суммы
    # Сначала рассчитываем префиксные суммы для всей матрицы, затем делаем запрос по префиксным суммам
    prefix_matrix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            prefix_matrix[i + 1][j + 1] = prefix_matrix[i][j + 1] + prefix_matrix[i + 1][j] + matrix[i][j] - \
                                          prefix_matrix[i][j]

    def get_subsum_prefix(x1, y1, x2, y2):
        subsum = prefix_matrix[x2][y2] - prefix_matrix[x1 - 1][y2] - prefix_matrix[x2][y1 - 1] + prefix_matrix[x1 - 1][
            y1 - 1]
        return subsum

    sum_responses = []
    for request in requests:
        subsum = get_subsum_prefix(*request)
        sum_responses.append(subsum)
    return sum_responses


def main():
    # считываем входные данные
    n, m, k, matrix, requests = load_data(INPUT_FILE)
    # Расчет суммы в прямоугольнике
    sum_responses = calc_sum(n, m, k, matrix, requests)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(map(str, sum_responses)))


if __name__ == "__main__":
    main()
