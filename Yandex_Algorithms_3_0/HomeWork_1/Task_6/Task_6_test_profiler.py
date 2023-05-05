# https://contest.yandex.ru/contest/45468/problems/6/
# 6. Операционные системы lite

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        m = int(file.readline())
        n = int(file.readline())
        partition_pairs = []
        for _ in range(n):
            partition_pairs.append(list(map(int, file.readline().split())))
    return m, n, partition_pairs


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет кол-ва работающих ОС
def calc_count_OS(m, n, partition_pairs):
    '''
    входные данные
    :m — количество секторов на жестком диске
    :n — количество созданых разделов
    :partition_pairs - N пар чисел ai и bi, задающих номера начального и конечного секторов раздела

    выходные данные
    :count_OS - количество работающих операционных систем
    '''
    working_os = []
    # print(m, n, partition_pairs)
    for i in range(n):
        # print(f"working_os: {working_os}")
        new_os = partition_pairs[i]
        # print(f"new_os: {new_os}")
        deleted_os_list = []
        for idx_os in range(len(working_os)):
            os = working_os[idx_os]
            # print(f"old_os: {os}")
            if new_os[0] <= os[0] <= new_os[1] or new_os[0] <= os[1] <= new_os[1] or os[0] <= new_os[0] <= os[1] or os[0] <= new_os[1] <= os[1]:
                # print(f"delete old_os: {os}")
                # deleted_os_list.append(idx_os)
                deleted_os_list.append(os)
        working_os.append(new_os)
        deleted_os_list = sorted(deleted_os_list, reverse=True)
        # print(f"deleted_os_list: {deleted_os_list}")
        for os in deleted_os_list:
            working_os.remove(os)
        # print(f"working_os after del: {working_os}")
    count_os = len(working_os)
    # print(f"count_os: {count_os}")
    return count_os


def main():
    # считываем входные данные
    m, n, partition_pairs = load_data(INPUT_FILE)
    # Расчет кол-ва работающих ОС

    count_os = calc_count_OS(m, n, partition_pairs)
    # print(f"count_os: {count_os}")
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_os))


import pytest


@pytest.mark.parametrize(
    "numbers, pairs, target_count_os",
    [
        ([10, 1], [[1, 1]], 1),
        ([10, 3], [[2, 2], [2, 2], [2, 2]], 1),
        ([10, 2], [[1, 1], [2, 2]], 2),
        ([10, 3], [[1, 1], [2, 2], [1, 3]], 1),
        ([10, 3], [[1, 3], [4, 7], [3, 4]], 1),
        ([1000000000, 0], [], 0),
        ([10, 4], [[1, 3], [4, 5], [7, 8], [4, 6]], 3),
        ([10, 3], [[8, 10], [2, 9], [1, 3], ], 1),

    ]
)
def test_calc_count_OS(numbers, pairs, target_count_os):
    count_os = calc_count_OS(numbers[0], numbers[1], pairs)
    print(f"count_os: {count_os}, target_count_os:{target_count_os}")
    assert count_os == target_count_os


if __name__ == "__main__":
    main()
    pytest.main(args=[__file__])
    #
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_stickers)
    # lp_wrapper(n, diego_stickers, count_guests, limits_sticker_guests)
    # lp.print_stats()

    # from random import randint
    # m = 10**9
    # n = 100
    # partition_pairs = [[randint(1, 10 ), randint(1, 10 )] for _ in range(n)]
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_count_OS)
    # lp_wrapper(m, n, partition_pairs)
    # lp.print_stats()