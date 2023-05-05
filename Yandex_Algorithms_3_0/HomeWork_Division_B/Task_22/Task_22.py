# https://contest.yandex.ru/contest/45468/problems/22/
# Дивизион  B
# 22. Кузнечик
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, k = map(int, file.readline().split())
    return n, k


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет прыжков
def calc_jumps(n, k):
    '''
    входные данные
    :n — длина доски
    :k - 1,2, ... , k - кол-во клеток на которые можно прыгать

    выходные данные
    :count_variants - кол-во вариантов добраться до последней клетке
    '''
    # По сути варианты прыжков на определенную клетку это сумма всех вариантов прыжков с других клеток для которых посчитано
    # База для динамического программирования
    # Заполняем начальные значения прыжков
    if n <= k:
        k = n-1
    dp = [1]
    for i in range(1, k):
        sub_sum = 0
        j = i - 1
        while j >= 0:
            sub_sum += dp[j]
            j -= 1
        dp.append(sub_sum + 1)
    # Теперь заполняем оставшиеся значения с помощью дин. программирования
    for i in range(k, n - 1):
        sub_sum = 0
        for j in range(i - 1, i - k - 1, -1):
            sub_sum += dp[j]
        dp.append(sub_sum)
    count_variants = dp[-1]
    return count_variants


def main():
    # считываем входные данные
    n, k = load_data(INPUT_FILE)
    # Расчет прыжков
    count_variants = calc_jumps(n, k)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_variants))


if __name__ == "__main__":
    main()
