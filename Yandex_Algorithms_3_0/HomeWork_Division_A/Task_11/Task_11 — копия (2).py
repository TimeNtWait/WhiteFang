# https://contest.yandex.ru/contest/45469/problems/11/
# Дивизион A
# 11. Конвейер


PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    transporters = []
    with open(filename, "r") as file:
        n = int(file.readline())
        for _ in range(n):
            container_test = [float(c) for c in file.readline().strip().split()]
            transporters.append([int(container_test[0]), container_test[1:]])
    return n, transporters


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Проверка упорядочиваемости контейниров на конвеере
def check_transporter(n, transporters):
    '''
    входные данные
    :n — количество тестов (конвееров)
    :transporters - конвееры с указанием кол-ва контейнеров в последовательности и K действительных чисел —
    степеней срочности контейнеров в порядке их поступления из цеха А

    выходные данные
    :result_check_transporters - массив ответов по каждому конвееру
    '''
    result_check_transporters = []
    # transporters
    for transporter in transporters:
        stack_A = transporter[1]
        stack_buffer = []
        stack_B = []
        container_is_sorted = 1
        while len(stack_A) > 0 or len(stack_buffer) > 0:
            # Перегоняем контейнеры из цеха А в цех B
            i = 0
            while i < len(stack_A):
                item = stack_A[i]
                if item == min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or item <= stack_buffer[0]):
                    stack_B.append(stack_A.pop(0))
                else:
                    break
                i += 1
            # Перегоняем контейнеры из цеха А на склад
            i = 0
            while i < len(stack_A):
                item = stack_A[i]
                if item != min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or (item <= stack_buffer[-1])):
                    stack_buffer.append(stack_A.pop(0))
                    i -= 1
                else:
                    break
                i += 1
            # Перегоняем контейнеры со склада в цех B
            i = len(stack_buffer) - 1
            while i >= 0:
                item = stack_buffer[i]
                if item == min(stack_A + stack_buffer):
                    stack_B.append(stack_buffer.pop())
                else:
                    break
                i -= 1
            # Если среди первых элементов в цехе А и складе лежит не самый минимальный элемент, то отсортировать нельзя
            if (len(stack_A) != 0 or len(stack_buffer) != 0) and min(stack_A[0:1] + stack_buffer[0:1]) != min(
                    stack_A + stack_buffer):
                container_is_sorted = 0
                break
        result_check_transporters.append(container_is_sorted)
    return result_check_transporters


def main():
    # считываем входные данные
    n, transporters = load_data(INPUT_FILE)
    # Проверка упорядочиваемости контейниров на конвеере
    result_check_transporters = check_transporter(n, transporters)
    print("\n".join(map(str, result_check_transporters)))
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(map(str, result_check_transporters)))


if __name__ == "__main__":
    main()
