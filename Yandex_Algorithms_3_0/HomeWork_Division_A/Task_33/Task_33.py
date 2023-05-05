# https://contest.yandex.ru/contest/45469/problems/33/
# Дивизион A
# 33. Радио Байтик
from sys import setrecursionlimit

# Снимаем ограничеи на кол-во рекурсий
setrecursionlimit(200000)
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        points = []
        for _ in range(n):
            points.append(tuple(map(int, file.readline().split())))
    return n, points


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# # Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
def dfs_stack(graph, n, visited, vertex, check_length):
    stack = [vertex]
    last_index = 1
    while len(stack) > 0:
        select_v = stack.pop()
        new_color = 3 - visited[select_v]
        for vv in range(last_index, n):
            if visited[vv] == 0 and graph[select_v][vv] < check_length:
                visited[vv] = new_color
                stack.append(vv)
        if len(stack) == 0:
            if 0 in visited:
                last_index = visited.index(0)
                visited[last_index] = 1
                stack.append(last_index)


# Расчет оптимальной мощности радио
def calc_radio_power(n, points):
    '''
    входные данные
    :n — количество вышек
    :points — координаты вышек

    выходные данные
    :radio_power – оптимальная мощность радио
    '''
    # Формируем полный граф
    graph = [[-1] * n for _ in range(n)]
    src_visited = [0] * n
    lengths = set([])
    for i in range(n - 1):
        for j in range(i + 1, n):
            graph[i][j] = graph[j][i] = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            lengths.add(graph[i][j])
    src_visited[0] = 1
    lengths = list(lengths)
    lengths.sort()

    def check_valid_length(visited, check_length):
        for i in range(n - 1):
            for j in range(i + 1, n):
                if graph[i][j] < check_length and visited[i] == visited[j]:
                    return False
        return True

    l = 0
    r = len(lengths) - 1
    true_length = 0
    true_choice = []
    while l < r:
        m = (l + r + 1) // 2
        check_length = lengths[m]
        visited = src_visited.copy()
        dfs_stack(graph, n, visited, 0, check_length)
        is_check = check_valid_length(visited, check_length)
        if is_check:
            l = m
            true_length = lengths[m]
            true_choice = visited.copy()
        else:
            r = m - 1
    true_length = round((true_length ** (1 / 2)) / 2, 15)
    radio_power = f"{true_length}\n" + " ".join(map(str, true_choice))
    return radio_power


def main():
    # считываем входные данные
    n, points = load_data(INPUT_FILE)
    # Расчет оптимальной мощности радио
    radio_power = calc_radio_power(n, points)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(radio_power))


if __name__ == "__main__":
    main()
