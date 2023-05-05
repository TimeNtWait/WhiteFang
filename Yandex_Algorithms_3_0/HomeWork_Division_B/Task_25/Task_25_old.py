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
    # База для динамического программирования

    min_thread_nails = [0]*(n+1)
    if n == 2:
        return nails[1]-nails[0]
    min_thread_nails[1] = nails[1] - nails[0]
    for i in range(2, n  ):
        pre_nail = (nails[i] - nails[i - 1])
        pre_pre_nail = (nails[i-1] - nails[i - 2])
        print(f"i: {i}, nails[i]: {nails[i]}, {n - 1}")
        if i == n - 1:
            post_pre = pre_nail + 1
        else:
            post_pre = (nails[i + 1] - nails[i])


        # print(f"pre_pre_nail:{pre_pre_nail}, pre_nail: {pre_nail}, post_pre: {post_pre}")
        if min_thread_nails[i-1] != 0 and pre_nail > post_pre:
            continue
        if min_thread_nails[i-1] == 0 and min_thread_nails[i-2] == 0:
            print(f"min_thread_nails[i-1] == 0: {pre_nail}")
            min_thread_nails[i] = pre_nail
            continue
        if pre_nail <= pre_pre_nail: # and pre_nail < post_pre:
            # print(f"pre_nail <= pre_pre_nail and pre_nail < post_pre:: {pre_nail}")
            min_thread_nails[i] = pre_nail
        elif pre_pre_nail <= pre_nail:
        # else:
            print(f"else : {pre_pre_nail}")
            min_thread_nails[i-1] = pre_pre_nail

    min_thread_nails[n] = nails[-1]-nails[-2]
    print(f"sum: {sum(min_thread_nails)}, min_thread_nails: {min_thread_nails}")
    return sum(min_thread_nails)


def main():
    # считываем входные данные
    n, nails = load_data(INPUT_FILE)
    # Суммарная длина нитки для гвоздиков
    thread_nails = calc_thread_nails(n, nails)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(thread_nails))


if __name__ == "__main__":
    main()
