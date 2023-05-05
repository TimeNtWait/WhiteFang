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
    delta_nails = [0] + [nails[i] - nails[i-1] for i in range(1,n)]

    print(delta_nails)
    print((n, nails))
    # База для динамического программирования

    min_thread_nails = [0]*(n+1)
    thread_nails = [0]
    if n == 2:
        return nails[1]-nails[0]
    thread_nails.append(nails[1]-nails[0])
    sum_thread_nails = nails[1]-nails[0]
    min_thread_nails[1] = nails[1] - nails[0]
    select_nails = {0, 1}

    min_sum = nails[1] - nails[0]
    for i in range(2, len(delta_nails)-1):
        print(f"i: {i}, delta_nails: {delta_nails[i]}, min_thread_nails[i]: {min_thread_nails[i]}")
        if delta_nails[i] < delta_nails[i+1] or min_thread_nails[i-1] == 0:
            min_thread_nails[i] = delta_nails[i]
        if delta_nails[i] < (delta_nails[i-1] + delta_nails[i+1]):
            # if min_thread_nails[i-2] != 0:
            #     min_thread_nails[i-1] = 0
            min_thread_nails[i] = delta_nails[i]

        # мин(I, i + 1) or i - 1 == 0
        # if min_thread_nails[i-1] != 0:
        #     if delta_nails[i] < delta_nails[i+1] and delta_nails[i+1] > delta_nails[i+2] :
        #         min_thread_nails[i] = delta_nails[i]
        # if delta_nails[i] < delta_nails[i + 1] and delta_nails[i + 1] > delta_nails[i + 2]:
        #     min_thread_nails[i] = delta_nails[i]
        # if min_thread_nails[i-1] == 0:
        #     min_thread_nails[i] = delta_nails[i]
        print(f"min_thread_nails: {min_thread_nails}")


    return 0


    for i in range(2, n - 2 ):
        print(f"i:{i}")
        # print(f"nails[i-1]:{nails[i-1]}, nails[i]:{nails[i]}, nails[i+1]:{nails[i+1]}")
        # print(f"(nails[i] - nails[i-1]): {(nails[i] - nails[i-1])}, (nails[i+1] - nails[i]): {(nails[i+1] - nails[i])}")

        pre_nail = (nails[i] - nails[i - 1])
        pre_pre_nail = (nails[i-1] - nails[i - 2])
        post_pre = (nails[i + 1] - nails[i])
        post_post_pre = (nails[i + 2] - nails[i+1])
        if min_thread_nails[i-1] == 0:
            min_thread_nails[i] = pre_nail
            sum_thread_nails += pre_nail
            thread_nails.append(pre_nail)
            continue

        # else:
        # elif pre_nail > post_pre:
        #     min_thread_nails[i] = -2
        #     continue
        print(f"____ pre_nail: {pre_nail} > post_pre: {post_pre}")


        # else:
        #     post_pre = (nails[i+1] - nails[i])
        #     if pre_nail < post_pre:
        #         min_thread_nails[i] = pre_nail
        #         sum_thread_nails += pre_nail
        #         thread_nails.append(pre_nail)
        #     continue
        if pre_nail <= pre_pre_nail and pre_nail < post_pre:
            print(f"pre_nail <= pre_pre_nail ")
            # select_nails.add(i)
            # select_nails.add(i-1)
            min_thread_nails[i] = pre_nail
            sum_thread_nails += pre_nail
            thread_nails.append(pre_nail)
        elif  pre_nail < post_pre and min_thread_nails[i-1] != 0 and  post_pre:
            print(f"pre_nail <= pre_pre_nail ")
            min_thread_nails[i] = pre_nail
            sum_thread_nails += pre_nail
            thread_nails.append(pre_nail)
        else :
            print(f"else : pre_nail <= pre_pre_nail ")
            # select_nails.add(i-2)
            # select_nails.add(i-1)
            min_thread_nails[i-1] = pre_pre_nail
            sum_thread_nails += pre_pre_nail
            thread_nails.append(pre_pre_nail)

        print(f"nails: {nails[i]}")
        print(f"pre_pre_nail: {pre_pre_nail}, pre_nail: {pre_nail}")
        print(f"min_thread_nails: {min_thread_nails}")


        continue
        #
        # pre_pre_nail = (nails[i] - nails[i - 1])
        # post_nail = (nails[i + 1] - nails[i])
        # post_pre = (nails[i+1] - nails[i - 1])
        # if post_pre - pre_nail <= post_nail:
        #     select_nails.add(i-1)
        #     select_nails.add(i+1)
        #     min_thread_nails[i+1] = post_pre
        #     sum_thread_nails += post_pre
        #     thread_nails.append(post_pre)
        #     continue
        #
        # if i in select_nails:
        #     continue
        # print(f"true i:{i}")
        # # if i in select_nails and min_thread_nails[i] <= min(pre_nail, post_nail, post_pre):
        # #     continue
        # print(f"nails: {nails[i]}")
        # print(f"___pre_nail: {pre_nail}, post_nail:{post_nail}, post_pre: {post_pre}")
        # min_len_thread = min(pre_nail, post_nail, post_pre)
        # if pre_nail <= post_nail and pre_nail <= post_pre:
        #     select_nails.add(i-1)
        #     select_nails.add(i)
        # elif post_pre <= post_nail:
        #     select_nails.add(i-1)
        #     select_nails.add(i + 1)
        # else:
        #     select_nails.add(i)
        #     select_nails.add(i+1)
        # min_thread_nails[i] = min_len_thread
        # # thread_nails.append(nails[1] - nails[0])
        # # min_len_thread = min((nails[i] - nails[i-1]), (nails[i+1] - nails[i]))
        # sum_thread_nails += min_len_thread
        # # print(f"min_len_thread: {min_len_thread}")
        # thread_nails.append(min_len_thread)
        # print(f"______________")


    thread_nails.append(nails[-1]-nails[-2])
    sum_thread_nails += nails[-1]-nails[-2]
    min_thread_nails[n] = nails[-1]-nails[-2]

    print(f"thread_nails: {thread_nails}")
    print(sum(thread_nails))
    print(f"min_thread_nails: {min_thread_nails}")
    print(sum(min_thread_nails))
    print(f"sum_thread_nails: {sum_thread_nails}")
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
