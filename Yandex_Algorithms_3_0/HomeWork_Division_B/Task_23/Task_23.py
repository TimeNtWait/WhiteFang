# https://contest.yandex.ru/contest/45468/problems/23/
# Дивизион  B
# 23. Калькулятор
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
    return n


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Расчет минимального кол-ва операций
def calc_min_operations(n):
    '''
    входные данные
    :n — искомое число

    выходные данные
    :min_operations - минимальное кол-ва операций для получения из 1 числа N
    '''

    # База для динамического программирования
    count_min_operations = [0, 0, 1, 1]  # 0, 1, 2, 3
    src_path = [0, 0, 1, 1]
    if n == 1:
        return [0, [1]]
    elif n <= 3:
        return [1, [1, n]]
    for i in range(4, n + 1):
        plus = count_min_operations[i - 1]
        if i % 2 == 0:
            mul2 = count_min_operations[i // 2]
        else:
            mul2 = n
        if i % 3 == 0:
            mul3 = count_min_operations[(i) // 3]
        else:
            mul3 = n
        count_min_operations.append(min([plus, mul2, mul3]) + 1)

        if plus <= mul3:
            if plus <= mul2:
                pre_i = i - 1
            elif mul2 < plus:
                pre_i = i // 2
        else:
            pre_i = i // 3
        src_path.append(pre_i)

    # Восстанавливаем путь
    path = [n]
    i = n
    while i > 1:
        i = src_path[i]
        path.append(i)
    return [count_min_operations[-1], reversed(path)]

# ошибка в тестах, почему-то не проходит 3ий тест
# 17
# 1 3 9 27 54 55 165 495 1485 4455 13365 26730 26731 80193 80194 80195 240585 481170 962340
# воспроизвести можно использовав if plus < mul2:     if plus < mul3:         pre_i = i - 1     elif mul3 < plus:         pre_i = i // 3 else:     pre_i = i // 2

def main():
    # считываем входные данные
    n = load_data(INPUT_FILE)
    # Расчет минимального кол-ва операций
    count_oper, path = calc_min_operations(n)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(count_oper) + "\n" + " ".join(map(str, path)))


if __name__ == "__main__":
    main()
