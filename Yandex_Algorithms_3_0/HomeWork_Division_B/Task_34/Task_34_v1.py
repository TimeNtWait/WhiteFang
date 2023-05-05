# https://contest.yandex.ru/contest/45468/problems/34/
# Дивизион  B
# 34. Топологическая сортировка
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
def create_orient_graph(edges):
    graph = {}
    for v1, v2 in edges:
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
    return graph


# Топологическая сортировка
def topology_sort(n, m, edges):
    '''
    входные данные
    :n — количество вершин в графе
    :m — количество ребер в графе
    :edges — ребра графа

    выходные данные
    :sorted_graph - Топологически сортированный граф
    '''
    graph = create_orient_graph(edges)
    visited = {}
    for v in range(1, n + 1):
        visited[v] = 0
    print(edges)
    print(graph)
    vertex_linkes = {}
    for v in graph:
        vertex_linkes[v] = len(graph[v])
    print(vertex_linkes)
    vertexes = []
    none_cycle = True
    for v in range(1, n + 1):
        if visited[v] == 0:
            none_cycle = dfs(graph, v, visited, vertexes)
            if not none_cycle:
                return "-1"
            vertexes.append(v)
    vertexes.reverse()
    print(f"vertexes: {vertexes}")
    print(f"none_cycle: {none_cycle}")
    return " ".join(map(str, vertexes))

def dfs(graph, vertex, visited, vertexes):
    none_cycle = True
    for v in graph[vertex]:
        if visited[v] == 0:
            visited[v] = 1
            if v in graph:
                none_cycle = dfs(graph, v, visited, vertexes)
            visited[v] = 2
            vertexes.append(v)
        elif visited[v] == 1:
            print(f"vertex: {vertex} v:{v}")
            none_cycle = False
        if not none_cycle:
            return none_cycle
    return none_cycle

def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Топологическая сортировка
    sorted_graph = topology_sort(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sorted_graph))


if __name__ == "__main__":
    main()
