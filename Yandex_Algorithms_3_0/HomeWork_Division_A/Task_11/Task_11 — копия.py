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
    print(n, transporters)
    # transporters = transporters[4:]
    for transporter in transporters:
        # container = transporter[1]
        # print(f"container: {container}")
        # stack_A = container[1]
        stack_A = transporter[1]

        stack_buffer = []
        stack_B = []
        container_is_sorted = 1
        print(f"init stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
        while len(stack_A) > 0 or len(stack_buffer) > 0:
            print(f"start stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # Перегоняем контейнеры из цеха А в цех B
            i = 0
            while i < len(stack_A) :
                item = stack_A[i]
                if item == min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or item < stack_buffer[0]):
                    stack_B.append(stack_A.pop(0))
                else:
                    break
                i += 1
            print(f"1 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")

            # Перегоняем контейнеры из цеха А на склад
            i = 0
            while i < len(stack_A):
                item = stack_A[i]
                print(f"item: {item}")
                if item != min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or (item < stack_buffer[-1])):
                    stack_buffer.append(stack_A.pop(0))
                    i -= 1
                else:
                    break
                i += 1
            print(f"2 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")

            # Перегоняем контейнеры со склада в цех B
            i = len(stack_buffer) - 1
            while i >= 0:
                item = stack_buffer[i]
                if item == min(stack_A + stack_buffer):
                    stack_B.append(stack_buffer.pop())
                else:
                    break
                i -= 1
            print(f"3 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # Если среди первых элементов в цехе А и складе лежит не самый минимальный элемент, то отсортировать нельзя
            if (len(stack_A) != 0 or len(stack_buffer) != 0) and  min(stack_A[0:1] + stack_buffer[0:1]) != min(stack_A + stack_buffer):
                container_is_sorted = 0
                break
        result_check_transporters.append(container_is_sorted)

    print(f"result_check_transporters: {result_check_transporters}")
    return 1
    stack_A = container[1:]
    stack_Stock = []
    stack_B = []
    while len(stack_way_1) > 0:
        # Перегоняем вагоны из 1 пути в тупик
        stack_stop_way.append(stack_way_1.pop(0))
        i = len(stack_way_1) - 1
        while i >= 0:
            wagon = stack_way_1[i]
            if wagon < stack_stop_way[-1]:
                stack_stop_way.append(stack_way_1.pop(0))
            i -= 1
        # Перегоняем вагоны из тупика на 2ой путь
        if len(stack_way_2) == 0 or (stack_stop_way[-1] > stack_way_2[-1] and (len(stack_way_1) == 0 or stack_stop_way[-1] < stack_way_1[0])):
            stack_way_2.append(stack_stop_way.pop())
        else:
            return "NO"
        i = len(stack_stop_way) - 1
        while i >= 0:
            wagon = stack_stop_way[i]
            if wagon > stack_way_2[-1] and (len(stack_way_1) == 0 or wagon < stack_way_1[0]):
                stack_way_2.append(stack_stop_way.pop())
            i -= 1
        # Если получилось что в тупике есть вагон который больше чем вагон на пути 2 то значит нельзя отсортировать
        if len(stack_stop_way) != 0 and stack_way_2[-1] > stack_stop_way[-1]:
            return "NO"
    return "YES"


def main():
    # считываем входные данные
    n, transporters = load_data(INPUT_FILE)
    # Проверка упорядочиваемости контейниров на конвеере
    is_check_sorted = check_transporter(n, transporters)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(is_check_sorted))


if __name__ == "__main__":
    main()
