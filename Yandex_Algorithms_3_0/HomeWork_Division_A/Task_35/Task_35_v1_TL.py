# https://contest.yandex.ru/contest/45469/problems/35/
# Дивизион A
# 35. Кружки в Маховниках
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
        courses = []
        for _ in range(n):
            row = file.readline().split()
            row = list(map(int, row))
            courses.append(row[1:])
    return n, courses


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Формируем граф из списка ребер
def create_orient_graph(courses):
    graph = {}
    for i in range(len(courses)):
        graph[i + 1] = []
    for i, course in enumerate(courses):
        for c in course:
            graph[c].append(i + 1)
    return graph


# Производим топологическую сортировку
def dfs(graph, vertex, visited, vertexes):
    for v in graph[vertex]:
        if not visited[v]:
            dfs(graph, v, visited, vertexes)
            visited[v] = True
            vertexes.append(v)


# Составление расписания по прохождению курсов
def sort_courses(n, courses):
    '''
    входные данные
    :n  — кол-во курсов
    :courses — список курсов. Первое значение это кол-во курсов, далее их требования по колву пройденых ранее курсов

    выходные данные
    :sorted_courses – количество пустых клеток в данной комнате.
    '''
    if n == 0:
        return ""

    # Составляем ориентированый граф
    graph = create_orient_graph(courses)

    # Сортируем расположение вершин в графе для более оптимального распределения
    for key in graph.keys():
        graph[key] = sorted(graph[key], reverse=True)
    src_visited = {}
    for v in range(1, n + 1):
        src_visited[v] = False

    # Производим топологическую сортировку
    all_vertexes = []
    for v in range(1, n + 1):
        visited = src_visited.copy()
        vertexes = []
        if not visited[v]:
            dfs(graph, v, visited, vertexes)
            vertexes.append(v)
            visited[v] = True
        vertexes.reverse()
        all_vertexes.append(vertexes)
    sorted_courses = []
    while len(sorted_courses) < n:
        max_item = 0
        for v in all_vertexes:
            while len(v) > 0 and v[-1] in sorted_courses:
                v.pop()
            if len(v) > 0:
                max_item = max(max_item, v[-1])

        if max_item > 0 and max_item not in sorted_courses:
            sorted_courses.append(max_item)
    sorted_courses.reverse()
    return " ".join(map(str, sorted_courses))


def main():
    # считываем входные данные
    n, courses = load_data(INPUT_FILE)
    # Составление расписания по прохождению курсов
    sorted_courses = sort_courses(n, courses)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sorted_courses))


if __name__ == "__main__":
    main()
