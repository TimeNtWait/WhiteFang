# https://contest.yandex.ru/contest/45468/problems/28/
# Дивизион  B
# 28. Ход конём
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
    for i in range(n - 1):
        for j in range(m - 1):
            if dp[i][j] == 0:
                continue
            if n - 1 >= i + 2:
                dp[i + 2][j + 1] = dp[i + 2][j + 1] + dp[i][j]
            if m - 1 >= j + 2:
                dp[i + 1][j + 2] = dp[i + 1][j + 2] + dp[i][j]
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
