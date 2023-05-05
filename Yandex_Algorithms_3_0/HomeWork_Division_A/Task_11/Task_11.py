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
    # transporters = transporters[1:2]
    for transporter in transporters:
        stack_A = transporter[1]
        stack_buffer = []
        stack_B = []
        sorted_transporter = sorted(transporter[1])
        current_min_index = 0
        container_is_sorted = 1
        # print(f"init stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
        # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
        # tmp = 0
        while len(stack_A) > 0 or len(stack_buffer) > 0:
            # tmp += 1
            # if tmp > 4:
            #     return [2]
            # print(f"start stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
            # Перегоняем контейнеры из цеха А в цех B
            i = 0
            while i < len(stack_A):
                item = stack_A[i]
                # if item == min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or item <= stack_buffer[0]):
                if item == sorted_transporter[current_min_index] and (
                        len(stack_buffer) == 0 or item <= stack_buffer[0]):
                    stack_B.append(stack_A.pop(0))
                    i -= 1
                    current_min_index += 1
                else:
                    break
                i += 1
            # print(f"1 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
            # Перегоняем контейнеры из цеха А на склад
            i = 0
            while i < len(stack_A):
                item = stack_A[i]
                # if item != min(stack_A + stack_buffer) and (len(stack_buffer) == 0 or (item <= stack_buffer[-1])):
                # if item != sorted_transporter[current_min_index] and (len(stack_buffer) == 0 or (item <= stack_buffer[-1])):
                if (len(stack_buffer) == 0 or (item <= stack_buffer[-1])):
                    stack_buffer.append(stack_A.pop(0))
                    i -= 1
                else:
                    break
                i += 1
            # print(f"2 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
            # Перегоняем контейнеры со склада в цех B
            i = len(stack_buffer) - 1
            while i >= 0:
                item = stack_buffer[i]
                # if item == min(stack_A + stack_buffer):
                if item == sorted_transporter[current_min_index]:
                    stack_B.append(stack_buffer.pop())
                    current_min_index += 1
                else:
                    break
                i -= 1
            # print(f"3 stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
            # Если переместить из цеха А на склад уже нельзя (т.е. например A[0] > S[-1])
            # И при этом A[0] и S[-1] не самые минимальные эелменты в цеху А и на складе, тогда
            # считаем, что отсортировать нельзя

            # Если переместить из цеха А на склад уже нельзя (т.е. например A[0] > S[-1])
            if len(stack_A) != 0 and len(stack_buffer) != 0 and stack_A[0] > stack_buffer[-1]:
                # И при этом A[0] и S[-1] не самые минимальные эелменты в цеху А и на складе, тогда отсортировать нельзя
                if min(stack_A[0], stack_buffer[-1]) != sorted_transporter[current_min_index]:
                    container_is_sorted = 0
                    break

            # if (len(stack_A) != 0 or len(stack_buffer) != 0) \
            #         and min(stack_A[:1] + stack_buffer[-1:]) != min(stack_A + stack_buffer):
            #     # and stack_A[0] + stack_buffer[-1]
            #
            #     container_is_sorted = 0
            #     break
            # print(f"end stack_B:{stack_B}, stack_buffer: {stack_buffer}, stack_A: {stack_A}")
            # print(f"len stack_B:{len(stack_B)}, stack_buffer: {len(stack_buffer)}, stack_A: {len(stack_A)}")
            # print("------------------")
        result_check_transporters.append(container_is_sorted)
    return result_check_transporters


def main():
    # считываем входные данные
    n, transporters = load_data(INPUT_FILE)
    # Проверка упорядочиваемости контейниров на конвеере
    result_check_transporters = check_transporter(n, transporters)
    #print("\n".join(map(str, result_check_transporters)))
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, "\n".join(map(str, result_check_transporters)))


if __name__ == "__main__":
    main()
