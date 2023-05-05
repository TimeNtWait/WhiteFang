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
    size_string = len(src_string)
    if size_string == 0:
        return 0
    max_len = 1
    for find_l in set(src_string):
        r = 0
        k = src_k + 0
        sub_len = 0
        if src_string[0] == find_l:
            sub_len = 1
        elif k > 0:
            k -= 1
            sub_len = 1
        for l in range(size_string):
            while r < size_string - 1:
                r += 1
                if src_string[r] == find_l:
                    sub_len += 1
                elif k > 0:
                    k -= 1
                    sub_len += 1
                else:
                    r -= 1
                    break
            max_len = max(max_len, sub_len)
            if r == size_string - 1:
                break
            sub_len -= 1
            if src_string[l] != find_l:
                k += 1
    return max_len


def main():
    # считываем входные данные
    k, src_string = load_data(INPUT_FILE)
    # Определяем кол-во операций для формирования новой строки
    max_len = calc_modify_string(k, src_string)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(max_len))


if __name__ == "__main__":
    main()
