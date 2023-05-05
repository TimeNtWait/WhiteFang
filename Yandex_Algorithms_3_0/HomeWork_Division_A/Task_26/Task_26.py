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

    i = 0
    for j in range(m):
        ii = i
        jj = j
        while jj >= 0 and ii < n:
            if ii - 2 >= 0:
                if jj - 1 >= 0:
                    dp[ii][jj] += dp[ii - 2][jj - 1]
                if jj + 1 < m:
                    dp[ii][jj] += dp[ii - 2][jj + 1]
            if jj - 2 >= 0:
                if ii - 1 >= 0:
                    dp[ii][jj] += dp[ii - 1][jj - 2]
                if ii + 1 < n:
                    dp[ii][jj] += dp[ii + 1][jj - 2]
            ii += 1
            jj -= 1

    j = m - 1
    for i in range(1, n):
        ii = i
        jj = j
        while jj >= 0 and ii < n:
            if ii - 2 >= 0:
                if jj - 1 >= 0:
                    dp[ii][jj] += dp[ii - 2][jj - 1]
                if jj + 1 < m:
                    dp[ii][jj] += dp[ii - 2][jj + 1]
            if jj - 2 >= 0:
                if ii - 1 >= 0:
                    dp[ii][jj] += dp[ii - 1][jj - 2]
                if ii + 1 < n:
                    dp[ii][jj] += dp[ii + 1][jj - 2]
            ii += 1
            jj -= 1

    min_step = dp[-1][-1]
    return min_step


def main():
    # считываем входные данные
    n, m = load_data(INPUT_FILE)
    # Расчет ходов конем
    count_steps = calc_horse_chess(n, m)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_steps))


if __name__ == "__main__":
    main()
