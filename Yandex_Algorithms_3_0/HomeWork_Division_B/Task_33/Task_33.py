# https://contest.yandex.ru/contest/45468/problems/33/
# Дивизион  B
# 33. Списывание
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


# Формируем граф из списка ребер
def create_graph(edges):
    graph = {}
    for v1, v2 in edges:
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        if v2 in graph:
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]
    return graph


# Определить дуальность графа
def is_dual_graph(n, m, edges):
    '''
    входные данные
    :n — количество вершин в графе
    :m — количество ребер в графе
    :edges — ребра графа

    выходные данные
    :is_dual - возможно ли разделить граф на две группы?
    '''
    graph = create_graph(edges)
    visited = {}
    for v in range(1, n + 1):
        visited[v] = 0

    vertex_component = {}
    for v in range(1, n + 1):
        if not visited[v]:
            if v in graph:
                is_dual = dfs(graph, v, visited, 1)
                if not is_dual:
                    return "NO"
    return "YES"


def dfs(graph, vertex, visited, type_group):
    is_dual = True
    for v in graph[vertex]:
        if visited[v] == 0:
            visited[v] = 3 - type_group
            is_dual = dfs(graph, v, visited, visited[v])
        elif visited[v] == type_group:
            is_dual = False
        if not is_dual:
            return is_dual
    return is_dual


def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Определить дуальность графа
    is_dual = is_dual_graph(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(is_dual))


if __name__ == "__main__":
    main()
