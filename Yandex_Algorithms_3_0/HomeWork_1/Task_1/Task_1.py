# Тренировки по алгоритмам 3.0 от Яндекса — Дивизион B
# https://contest.yandex.ru/contest/45468/problems/
# 1. Гистограмма

PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    input_text = ""
    with open(filename, "r") as file:
        input_text = file.readlines()
    input_text = ''.join(input_text)
    input_text = input_text.replace(" ", "").replace("\n", "")
    return input_text


# Вывод гистрограммы символов
def calc_task(input_text):
    '''
    входные данные
    :input_text - входной текст
    выходные данные
    :symbols_histogram - текст содержащий символьную гистрограмму
    '''
    symbols_counter = {}
    max_symbols = 0
    uniq_symbols = []
    for sym in input_text:
        if sym not in symbols_counter:
            symbols_counter[sym] = 1
            uniq_symbols.append(sym)
        else:
            symbols_counter[sym] += 1
        max_symbols = max(max_symbols, symbols_counter[sym])
    uniq_symbols = sorted(uniq_symbols)
    for row_index in range(max_symbols, 0, -1):
        for sym in uniq_symbols:
            if symbols_counter[sym] >= row_index:
                print("#", end="")
            else:
                print(" ", end="")
        print("\n", end="")
    print("".join(uniq_symbols), end="")


def main():
    # считываем входные данные
    input_text = load_data(INPUT_FILE)
    # Расчет
    # Вместо записи в файл будем делать сразу вывод, чтобы экономить память
    calc_task(input_text)


if __name__ == "__main__":
    main()
