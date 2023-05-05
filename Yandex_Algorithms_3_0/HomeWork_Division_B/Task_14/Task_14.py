# https://contest.yandex.ru/contest/45468/problems/14/
# Дивизион B
# 14. Сортировка вагонов lite


PATH = ""
INPUT_FILE = PATH + "input.txt"
OUTPUT_FILE = PATH + "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = file.readline().strip()
        wagons = file.readline().strip().split()
        wagons = [int(w) for w in wagons]
    return n, wagons


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Проверка упорядочиваемости ваганов
def check_train_move(n, wagons):
    '''
    входные данные
    :n — количество вагонов в поезде (1 ≤ N ≤ 100)

    выходные данные
    :wagons - Результат проверки упорядочиваемости ваганов
    '''
    stack_way_1 = wagons
    stack_way_2 = []
    stack_stop_way = []
    while len(stack_way_1) > 0:
        # Перегоняем вагоны из 1 пути в тупик
        stack_stop_way.append(stack_way_1.pop(0))
        i = 0
        while i < len(stack_way_1):
            wagon = stack_way_1[i]
            if wagon < stack_stop_way[-1]:
                stack_stop_way.append(stack_way_1.pop(0))
            else:
                i += 1
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
    n, wagons = load_data(INPUT_FILE)
    # Проверка упорядочиваемости ваганов
    is_check_sorted = check_train_move(n, wagons)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(is_check_sorted))


if __name__ == "__main__":
    main()
