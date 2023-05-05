# https://contest.yandex.ru/contest/45468/problems/24/
# Дивизион  B
# 24. Покупка билетов
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        queue = [(0, 0, 0)]
        for _ in range(n):
            a, b, c = map(int, file.readline().split())
            queue.append((a, b, c))
    return n, queue


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет минимального времени для покупки билетов в очереди
def calc_min_time_queue(n, queue):
    '''
    входные данные
    :n — длина очереди
    :queue - затраты на покупку 1-го, 2-х, 3х биелтов для каждого человека

    выходные данные
    :min_time - минимальное время для покупки билетов для всей очереди
    '''

    # База для динамического программирования
    min_times = [0]
    min_times.append(queue[1][0])
    if n == 1:
        return min_times[1]

    min_times.append(min((queue[1][0] + queue[2][0]), queue[1][1]))
    if n == 2:
        return min_times[2]

    min_times.append(
        min((queue[1][0] + queue[2][0] + queue[3][0]), (queue[1][1] + queue[3][0]), (queue[1][0] + queue[2][1]),
            (queue[1][2])))
    if n == 3:
        return min_times[3]

    for i in range(4, n + 1):
        min_time_curent = min(
            min_times[i - 1] + queue[i][0],
            min_times[i - 2] + queue[i - 1][1],
            min_times[i - 3] + queue[i - 2][2],
        )
        min_times.append(min_time_curent)
    return min_times[-1]


def main():
    # считываем входные данные
    n, queue = load_data(INPUT_FILE)
    # Расчет минимального времени для покупки билетов в очереди
    min_time = calc_min_time_queue(n, queue)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(min_time))


if __name__ == "__main__":
    main()
