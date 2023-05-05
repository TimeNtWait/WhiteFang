# https://contest.yandex.ru/contest/45468/problems/29/
# Дивизион  B
# 29. Кафе
import math

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        costs = []
        for _ in range(n):
            costs.append(int(file.readline()))
    return n, costs


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет оптимальных затрат на кафе
def calc_min_cost(n, costs):
    '''
    входные данные
    :n — кол-во дней
    :costs — цена обеда за каждый день

    выходные данные
    :result - В первой строке выдайте минимальную возможную суммарную стоимость обедов.
                   Во второй строке выдайте два числа K1 и K2 — количество купонов, которые останутся
    '''
    if n == 0:
        return f"0\n0 0"
    if n == 1:
        if costs[0] > 100:
            return f"{costs[0]}\n1 0"
        else:
            return f"{costs[0]}\n0 0"
    dp = [[math.inf] * (n) for _ in range(n)]
    path_matrix = [[math.inf] * (n) for _ in range(n)]
    dp[0][0] = costs[0]
    if dp[0][0] > 100:
        dp[0][1] = costs[0]
    for i in range(1, n):
        for j in range(0, n-1):
            if costs[i] > 100 and j >=1 :
                if dp[i - 1][j-1] + costs[i] < dp[i - 1][j + 1]:
                    dp[i][j] = dp[i - 1][j-1] + costs[i]
                    path_matrix[i][j] = (i - 1, j - 1)
                else:
                    dp[i][j] = dp[i - 1][j + 1]
                    path_matrix[i][j] = (i - 1, j + 1)
            else:
                if dp[i - 1][j] + costs[i] < dp[i - 1][j + 1]:
                    dp[i][j] = dp[i - 1][j] + costs[i]
                    path_matrix[i][j] = (i - 1, j)
                else:
                    dp[i][j] = dp[i - 1][j + 1]
                    path_matrix[i][j] = (i - 1, j + 1)

    min_cost = dp[-1][0]
    save_coupons = 0
    for i in range(1, n):
        if dp[-1][i] <= min_cost:
            save_coupons += 1
    # Восстанавливаем путь
    path = [path_matrix[-1][save_coupons]]
    days = []
    if path_matrix[-1][save_coupons][1] > save_coupons:
        days.append(len(path_matrix))
    while path[-1][0] > 0:
        x = path[-1][0]
        y = path[-1][1]
        if path_matrix[x][y][1] > path[-1][1]:
            days.append(x + 1)
        path.append(path_matrix[x][y])

    result = str(min_cost)
    result += f"\n{save_coupons} {len(days)}"
    result += "\n" + "\n".join(map(str, sorted(days)))
    return result


def main():
    # считываем входные данные
    n, costs = load_data(INPUT_FILE)
    # Расчет оптимальных затрат на кафе
    min_cost = calc_min_cost(n, costs)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_cost))


if __name__ == "__main__":
    main()
