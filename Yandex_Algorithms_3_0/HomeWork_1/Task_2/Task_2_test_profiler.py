# https://contest.yandex.ru/contest/45468/problems/2/
# 2. Красивая строка

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        k = int(file.readline())
        src_string = file.readline().strip()
    return k, src_string


# # Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определяем кол-во операций для формирования новой строки
def calc_modify_string(src_k, src_string):
    '''
    входные данные
    :src_k - кол-во допустимых модернизаций
    :src_string - исходная строка

    выходные данные
    :size_doubles_char - максимальное кол-во одинаковых символов подряд
    '''
    # Вариант:
    # 1. перевести все нужные символы в нули, а другие в 1
    # 2. сделать до масив с накопительной суммумой, для быстрого поиска суммы в интервале
    # 3. свдигая границы искать оптимальную длину с суммой = кол-во разрешенных для смены символов

    # for _ in range(100000):
        # 2.04115 s
        # for l in ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m",]:
        #     pass
        # 1.59753 s
        # for l in "qwertyuiopasdfghjklzxcvbnm":
        #     pass
        # 1.67252s
        # for i in range(ord('a'), ord('z') + 1):
        #     pass
            # print(chr(i))
    print(src_k, src_string)
    size_string = len(src_string)
    max_len = 1
    for find_l in set(src_string):
        print(f"find_l: {find_l}")
        r = 0
        k = src_k + 0
        # print(f"k: {k}, src_k:{src_k}")
        # src_string[0:r]
        sub_len = 0
        if src_string[0] == find_l:
            sub_len = 1
        elif k > 0:
            k -= 1
            sub_len = 1
        print(f"___l: {0}, r:{r}, sub_len: {sub_len}, max_len: {max_len}, find_l: {find_l}")
        for l in range(size_string):
            # print(l)
            while r < size_string -1:
                r += 1
                # print(r)
                # print(src_string[r])
                if src_string[r] == find_l:
                    sub_len += 1
                elif k > 0:
                    k -= 1
                    sub_len += 1
                else:
                    r -= 1
                    break
                # print(f"l: {l}, r:{r}, src_string[l:r]: {src_string[l:r+1]}, sub_len: {sub_len}")
            # if sub_len > max_len:
            #     print(f"l: {l}, r:{r}, k: {k}, sub_len: {sub_len}, max_len: {max_len}, find_l: {find_l}")
            max_len = max(max_len, sub_len)

            # print(f"l: {l}, r:{r}, k: {k}, sub_len: {sub_len}, max_len: {max_len}, find_l: {find_l}")
            # print(src_string[l:r])
            # print(f"l: {l}, r:{r}, sub_len: {sub_len}, max_len: {max_len}, find_l: {find_l}")
            if r == size_string - 1:
                break
            sub_len -= 1
            if src_string[l] != find_l:
                k += 1
            # print(f"l: {l}, r:{r}, sub_len: {sub_len}, max_len: {max_len}, find_l: {find_l}")
    print(f"max_len: {max_len}")
    return max_len



    # if k > len(string) - 1:
    #     return len(string)
    # # рассмотреть когда k = 0
    # # рассмотреть когда k = 1
    #     # не забыть изменять вне границ
    # # рассмотреть когда k = 2




def main():
    # считываем входные данные
    k, src_string = load_data(INPUT_FILE)
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_modify_string)
    # lp_wrapper(k, src_string)
    # lp.print_stats()


    # # Определеляем время движения поездов
    result_min_max_time = calc_modify_string(k, src_string)
    # Записываем результат в output.txt
    # save_output(OUTPUT_FILE, " ".join(map(str, result_min_max_time)))

#
# import pytest
#
#
# @pytest.mark.parametrize(
#     "numbers, target_min_max_time",
#     [
#         ([1, 3, 3, 2, ], [5, 7]),
#         ([1, 5, 1, 2, ], [-1]),
#         # ([3, 2, 7, 11, ], [27, 32]), - не верно
#         ([3, 2, 7, 11, ], [31, 31]),
#     ]
# )
# def test_calc_modify_string(numbers, target_min_max_time):
#     result_min_max_time = calc_modify_string(*numbers)
#     # print(f"result_min_max_time: {result_min_max_time}, target_min_max_time: {target_min_max_time}")
#     assert result_min_max_time == target_min_max_time


if __name__ == "__main__":
    main()
    # pytest.main(args=[__file__])
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(main)
    # lp_wrapper()
    # lp.print_stats()
