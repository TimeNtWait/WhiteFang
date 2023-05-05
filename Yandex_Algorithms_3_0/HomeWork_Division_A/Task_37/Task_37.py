# https://contest.yandex.ru/contest/45469/problems/37/
# Дивизион  A
# 37. Числа
from collections import deque

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n1 = file.readline().strip()
        n2 = file.readline().strip()
    return n1, n2


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(n1, n2):
    '''
    входные данные
    :n1 - первое число, в виде строки
    :n2 - второе число, в виде строки

    Правила преобразований:
    - Можно увеличить первую цифру числа на: 1, если она не равна 9.
    - Можно уменьшить последнюю цифру на 1, если она не равна 1
    - Можно циклически сдвинуть все цифры на одну вправо.
    - Можно циклически сдвинуть все цифры на одну влево.

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    # Формирование графа
    queue_bfs = deque()
    queue_bfs.append(n1)
    visited = {}
    visited[n1] = 0
    path = {}
    while len(queue_bfs) > 0:
        number = queue_bfs.popleft()
        dig_number = list(map(int, number))
        new_numbers = []

        if dig_number[0] < 9:
            new_numbers.append([dig_number[0] + 1] + dig_number[1:])
        if dig_number[-1] > 1:
            new_numbers.append(dig_number[:-1] + [dig_number[-1] - 1])
        new_numbers.append(dig_number[1:] + [dig_number[0]])
        new_numbers.append([dig_number[-1]] + dig_number[:-1])

        for numb in new_numbers:
            numb = "".join(map(str, numb))
            if numb not in visited or visited[numb] > visited[number] + 1:
                queue_bfs.append(numb)
                visited[numb] = visited[number] + 1
                path[numb] = number

    res_path = []
    current_v = n2
    while current_v != n1:
        res_path.append(current_v)
        current_v = path[current_v]
    res_path.append(n1)
    res_path.reverse()
    return "\n".join(res_path)


def main():
    # считываем входные данные
    n1, n2 = load_data(INPUT_FILE)
    # Поиск минимального пути
    length_route = find_path(n1, n2)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
