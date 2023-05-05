# https://contest.yandex.ru/contest/45469/problems/32/
# Дивизион A
# 32. Откуда достижима первая вершина
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        edges = []
        for _ in range(m):
            edges.append(tuple(map(int, file.readline().split())))
    return n, m, edges


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


def dfs(graph, vertex, visited, vertexes):
    if vertex not in graph:
        return
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            vertexes.append(v)
            dfs(graph, v, visited, vertexes)


# Формируем ориентированный граф из списка ребер но с указанием обратного направления
def create_graph(edges):
    graph = {}
    for v1, v2 in edges:
        if v2 in graph:
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]
    return graph


# Поиск вершин, из которых достижима первая
def find_vertex(n, m, edges):
    '''
    входные данные
    :n — количество вершин в графе
    :m — количество ребер в графе
    :edges — ребра графа

    выходные данные
    :res_vertexes – вершины, из которых достижима первая
    '''
    if n == 0:
        return ""
    elif m == 0:
        return "1"
    graph = create_graph(edges)
    if 1 not in graph:
        return "1"
    visited = {}
    for v in range(1, n + 1):
        visited[v] = False
    vertexes = [1]
    dfs(graph, 1, visited, vertexes)
    vertexes = sorted(set(vertexes))
    return " ".join(map(str, vertexes))


def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Поиск вершин, из которых достижима первая
    vertex = find_vertex(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(vertex))


if __name__ == "__main__":
    main()
