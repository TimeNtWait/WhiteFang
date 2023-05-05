# https://contest.yandex.ru/contest/45469/problems/26/
# Дивизион A
# 26. Ход конём - 2
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m = list(map(int, file.readline().split()))
    return n, m


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет ходов конем
def calc_horse_chess(n, m):
    '''
    входные данные
    :n, m — размер доски

    выходные данные
    :count_steps - количество способов добраться конём до правого нижнего угла доски.
    '''
    dp = [[0] * (m) for _ in range(n)]
    dp[0][0] = 1
    stack = [(0, 0)]
    while len(stack) > 0:
        i, j = stack.pop()
        if i + 2 <= n - 1:
            if j + 1 < m:
                dp[i + 2][j + 1] = dp[i + 2][j + 1] + 1
                stack.append((i + 2, j + 1))
            if j - 1 >= 0:
                dp[i + 2][j - 1] = dp[i + 2][j - 1] + 1
                stack.append((i + 2, j - 1))
        if j + 2 <= m - 1:
            if i + 1 < n:
                dp[i + 1][j + 2] = dp[i + 1][j + 2] + 1
                stack.append((i + 1, j + 2))
            if i - 1 >= 0:
                dp[i - 1][j + 2] = dp[i - 1][j + 2] + 1
                stack.append((i - 1, j + 2))

    for i in range(len(dp)):
        print(dp[i])
    min_step = dp[-1][-1]
    return min_step


def main():
    # считываем входные данные
    n, m = load_data(INPUT_FILE)
    # Расчет ходов конем
    count_steps = calc_horse_chess(n, m)

    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_horse_chess)
    # lp_wrapper(n, m)
    # lp.print_stats()

    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_steps))


if __name__ == "__main__":
    main()
