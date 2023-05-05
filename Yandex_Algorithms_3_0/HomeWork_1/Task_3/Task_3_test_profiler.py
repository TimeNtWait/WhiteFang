# https://contest.yandex.ru/contest/45468/problems/3/
# 3. Коллекционер Диего

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        diego_stickers = list(map(int, file.readline().split()))
        count_guests = int(file.readline())
        limits_sticker_guests = list(map(int, file.readline().split()))
    return n, diego_stickers, count_guests, limits_sticker_guests


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Определяем кол-во операций для формирования новой строки
def calc_stickers(n, diego_stickers, count_guests, limits_sticker_guests):
    '''
    входные данные
    :n - кол-во наклеек у Диего
    :diego_stickers - номера наклеек у Диего
    :count_guests - кол-во гостей
    :limits_sticker_guests - наименьшие номера наклеек, не интересующие гостей

    выходные данные
    :count_stickers_none_by_guest - кол-во различных чисел на наклейках, которые есть у Диего, но нет у гостя
    '''
    if count_guests == 0:
        return []
    if n == 0:
        return [0] * count_guests

    # По условию макс кол-во гостей равно макс кол-ву наклеек:
    # - Наивный вариант просто сделать перебор всех наклеек и всех гостей что будет N**2
    # - Варинат получше, делать сортировку O(N*logN) и делать бинарный поиск для всех гостей O(N*logN) итого O(2*N*logN)

    # Сортировка всех наклеек Диего для использования бинарного поиска
    # интересует кол-во !различных! чисел на наклейках
    diego_stickers = sorted(set(diego_stickers))
    stickers_for_guest = []
    for limit_by_guest in limits_sticker_guests:
        # Поиск кол-ва подходящих наклеек через бинарный поиск.
        l = 0
        r = len(diego_stickers) - 1
        while l != r:
            mid = (l + r + 1) // 2
            if diego_stickers[mid] < limit_by_guest:
                l = mid
            else:
                r = mid - 1
        # Если левая граница равна 0 и при этом значение не подходит, значит подходящих марок нет
        if l == 0 and diego_stickers[l] >= limit_by_guest:
            stickers_for_guest.append(0)
        else:
            stickers_for_guest.append(l + 1)
    return stickers_for_guest


def main():
    # считываем входные данные
    n, diego_stickers, count_guests, limits_sticker_guests = load_data(INPUT_FILE)
    # Определяем кол-во операций для формирования новой строки
    stickers_for_guest = calc_stickers(n, diego_stickers, count_guests, limits_sticker_guests)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(map(str, stickers_for_guest)))


if __name__ == "__main__":
    main()

    # from random import randint
    # n = 10000
    # diego_stickers = [randint(1, 10 ** 9) for _ in range(n)]
    # count_guests =10000
    # limits_sticker_guests = [randint(1, 10 ** 9) for _ in range(count_guests)]
    #
    # from line_profiler import LineProfiler
    #
    # lp = LineProfiler()
    # lp_wrapper = lp(calc_stickers)
    # lp_wrapper(n, diego_stickers, count_guests, limits_sticker_guests)
    # lp.print_stats()
