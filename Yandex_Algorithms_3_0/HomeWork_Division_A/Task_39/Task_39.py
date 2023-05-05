# https://contest.yandex.ru/contest/45469/problems/39/
# Дивизион  A
# 39. Роботы
import math
from collections import deque
import heapq

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, k = map(int, file.readline().split())
        edges = []
        for _ in range(k):
            row = list(map(int, file.readline().split()))
            edges.append(row)
        m = int(file.readline().strip())
        robots = list(map(int, file.readline().split()))
    return n, k, m, edges, robots


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Поиск минимального пути
def find_path(n, k, m, edges, robots):
    '''
    входные данные
    :n — количество залов
    :k — количество туннелей
    :m — количество роботов
    :edges — ребра соединяющие 2 вершины
    :robots - вершины в которых расположены роботы

    выходные данные
    :length_route - Длина кратчайшего пути
    '''
    # Важные примечания условия!
    # Туннель может соединять зал с самим собой
    # Условие либо роботы в одном зале тогда 0 шагов осталось, либо в двух залах соединенных тунелем тогда еще +1 шаг остался
    # Если роботы никогда не смогут собраться вместе, выведите одно число –1 - вероятно только в том случае когда они вернулись в исходное состояние
    # Туннель может соединять зал с самим собой, в таких тунелях роботы могут пережидать нужное время
    # Роботам чтобы вернуться в вершину надо 2 минуты туда и обратно
    # Для колец 1 минута
    # Также роботы могут быть в соседних вершинах чтобы потом встретиться по середине тогда 1 минута в соседнюю вершину и 1 на встречу в туннеле
    # 1. Найти минимальные времена посещения каждым роботом каждой вершины
    # 2. Искать минимальное время сбора на одной вершине,  если она кольцо то можно разницу по времени свести к самому долгом роботу. Искать соседние вершины с роботами минимальное время в каждой плюс 1 к итогу.
    # Алгоритм поиска:
    #    Берем максимальную цену посещения зала каким-либо роботом
    #    Если есть хотя бы один срок бесконечный (inf), тогда ответ -1, нельяз собрать всех вместе
    #    Проверяем все остальные времена посещения и сравниваем с максимальным
    #    Как можно добрать до нужного размера:
    #     - прибавлять 2 каждому времени за счет хождения робота в соседний зал и обратно (если у вершины есть хотя бы одно ребро)
    #     - прибавлять 1 каждому времени если в текущем зале есть кольцо (ребро само себя)
    #     - если нечетная разница то можно отправить всех роботов соседний зал и тогда чтобы они встретились на ребре просто к максимальному времени добавить 0.5
    #     - вообще может быть еще если большая нечетная разница то робот может обойти по циклу (если есть) и добавить +3 или больше (зависит от наличия соответсвтующих циклов)
    #     - может быть ситуация, что все рооты успевают за одно время, но один работ приходит на 1 минуту позже, по идеи, значит он был соседней вершине и тогда можно считать ответ как раз максимальное значение, но все усложняется если таких роботов много надо проверять какие значниея у них были в соседних клетках
    #     - может быть ситуация когда робот в одну и ту же вершину может придти либо за n либо за n+1, тогда надо это учитывать, можно либо пост проверкой или сразу искать
    #    Если есть хотя бы один срок бесконечный (inf), тогда ответ -1, нельяз собрать всех вместе
    #    но это допустимо если для этой вершины все роботы дают бесконечное время, если например вершина в другой компоеннте связанности
    #    Определяем максимальную цену посещения зала каким-либо роботом

    # Если роботы уже расставлены в одном зале тогда ноль перемещений
    if min(robots) == max(robots):
        return 0
    # Если тонелей нет, значит роботы не смогут перемещаться
    if k == 0:
        return -1

    # Формируем граф
    graph = {}
    vertexes = {}
    vertexes_info = {}
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = set([])
        if edge[1] not in graph:
            graph[edge[1]] = set([])
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
        vertexes[edge[0]] = (math.inf, math.inf)
        vertexes[edge[1]] = (math.inf, math.inf)

    # Обходим роботами все вершины
    for robot in robots:
        queue_bfs = deque()
        queue_bfs.append(robot)
        robot_vertexes = vertexes.copy()
        robot_vertexes[robot] = (0, math.inf)
        # Если робот находится в вершине, которая вне графа
        if robot not in graph:
            return -1
        while len(queue_bfs) > 0:
            point = queue_bfs.popleft()
            new_val_even = robot_vertexes[point][0] + 1
            new_val_odd = robot_vertexes[point][1] + 1
            for v in graph[point]:
                # ищем для каждой вершины четные и нечетные минимальные посещения.
                # можно исходить из того что +1 к посещению всегда меняет чет/нечет
                if new_val_even < robot_vertexes[v][1]:
                    robot_vertexes[v] = (robot_vertexes[v][0], new_val_even)
                    if v not in queue_bfs:
                        queue_bfs.append(v)
                if new_val_odd < robot_vertexes[v][0]:
                    robot_vertexes[v] = (new_val_odd, robot_vertexes[v][1])
                    if v not in queue_bfs:
                        queue_bfs.append(v)

        # Формируем массив нахождения всех роботов на каждой вершине
        for v in robot_vertexes:
            if v not in vertexes_info:
                vertexes_info[v] = [[], []]
            vertexes_info[v][0].append(robot_vertexes[v][0])
            vertexes_info[v][1].append(robot_vertexes[v][1])

    # Определяем время нахождения всех роботов на каждой вершине
    find_min_heap = []
    heapq.heapify(find_min_heap)
    # Встреча на вершине
    for v in graph.keys():
        heapq.heappush(find_min_heap, max(vertexes_info[v][0]))
        heapq.heappush(find_min_heap, max(vertexes_info[v][1]))

    # Встреча на ребре
    for v1, v2 in edges:
        heapq.heappush(find_min_heap, max(map(min, vertexes_info[v1][0], vertexes_info[v2][0])) + 0.5)
        heapq.heappush(find_min_heap, max(map(min, vertexes_info[v1][1], vertexes_info[v2][1])) + 0.5)

    length_route = heapq.heappop(find_min_heap)
    # print(f"length_route: {length_route}")
    # Если есть хотя бы один срок бесконечный (inf), тогда ответ -1, нельяз собрать всех вместе
    if math.isinf(length_route):
        return -1
    else:
        return length_route


def main():
    # считываем входные данные
    n, k, m, edges, robots = load_data(INPUT_FILE)
    # Поиск минимального пути
    length_route = find_path(n, k, m, edges, robots)

    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(length_route))


if __name__ == "__main__":
    main()
