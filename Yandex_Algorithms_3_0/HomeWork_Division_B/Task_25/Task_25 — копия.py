# https://contest.yandex.ru/contest/45468/problems/25/
# Дивизион  B
# 25. Гвоздики
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        nails = list(map(int, file.readline().split()))
    return n, nails


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Минимальная суммарная длина нитки для гвоздиков
def calc_thread_nails(n, nails):

    '''
    входные данные
    :n — кол-во гвоздей
    :nails - координаты гвоздей

    выходные данные
    :min_thread_nails - Минимальная суммарная длина нитки для гвоздиков
    '''
    nails = sorted(nails)
    print((n, nails))
    # База для динамического программирования

    min_thread_nails = [-1]*(n+1)
    thread_nails = [0]
    if n == 2:
        return nails[1]-nails[0]
    thread_nails.append(nails[1]-nails[0])
    sum_thread_nails = nails[1]-nails[0]
    min_thread_nails[2] = nails[1] - nails[0]
    select_nails = {0, 1}
    for i in range(2, n -2 ):
        print(f"i:{i}")
        # print(f"nails[i-1]:{nails[i-1]}, nails[i]:{nails[i]}, nails[i+1]:{nails[i+1]}")
        # print(f"(nails[i] - nails[i-1]): {(nails[i] - nails[i-1])}, (nails[i+1] - nails[i]): {(nails[i+1] - nails[i])}")
        pre_nail = (nails[i] - nails[i - 1])
        post_nail = (nails[i + 1] - nails[i])
        post_pre = (nails[i+1] - nails[i - 1])
        if post_pre - pre_nail <= post_nail:
            select_nails.add(i-1)
            select_nails.add(i+1)
            min_thread_nails[i+1] = post_pre
            sum_thread_nails += post_pre
            thread_nails.append(post_pre)
            continue

        if i in select_nails:
            continue
        print(f"true i:{i}")
        # if i in select_nails and min_thread_nails[i] <= min(pre_nail, post_nail, post_pre):
        #     continue
        print(f"nails: {nails[i]}")
        print(f"___pre_nail: {pre_nail}, post_nail:{post_nail}, post_pre: {post_pre}")
        min_len_thread = min(pre_nail, post_nail, post_pre)
        if pre_nail <= post_nail and pre_nail <= post_pre:
            select_nails.add(i-1)
            select_nails.add(i)
        elif post_pre <= post_nail:
            select_nails.add(i-1)
            select_nails.add(i + 1)
        else:
            select_nails.add(i)
            select_nails.add(i+1)
        min_thread_nails[i] = min_len_thread
        # thread_nails.append(nails[1] - nails[0])
        # min_len_thread = min((nails[i] - nails[i-1]), (nails[i+1] - nails[i]))
        sum_thread_nails += min_len_thread
        # print(f"min_len_thread: {min_len_thread}")
        thread_nails.append(min_len_thread)
        print(f"______________")


    thread_nails.append(nails[-1]-nails[-2])
    sum_thread_nails += nails[-1]-nails[-2]
    print(thread_nails)
    print(sum(thread_nails))
    print(min_thread_nails)
    print(sum(min_thread_nails))
    print(sum_thread_nails)
    return sum_thread_nails


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
    return thread_nails


def main():
    # считываем входные данные
    n, nails = load_data(INPUT_FILE)
    # Суммарная длина нитки для гвоздиков
    thread_nails = calc_thread_nails(n, nails)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(thread_nails))


if __name__ == "__main__":
    main()
