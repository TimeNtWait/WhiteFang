# https://contest.yandex.ru/contest/45468/problems/31/
# Дивизион  B
# 31. Поиск в глубину
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
        # if v1 == v2:
        #     continue
        if v1 in graph:
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        if v2 in graph:
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]
    return graph


# Построение компоненты связности
def find_componenta(n, m, edges):
    '''
    входные данные
    :n — количество вершин в графе
    :m — количество ребер в графе
    :edges — ребра графа

    выходные данные
    :describe_componenta - информация о компоненте связности: количество вершин + Вершины компоненты связности,
    перечисленные в порядке возрастания номеров.
    '''
    if n == 0:
        return "0"
    elif m == 0:
        return "1\n1"
    graph = create_graph(edges)
    if 1 not in graph:
        return "1\n1"
    visited = {}
    for v in graph.keys():
        visited[v] = False
    dfs(graph, 1, visited)
    vertexes = []
    for v in visited:
        if visited[v]:
            vertexes.append(v)
    vertexes.sort()
    describe_componenta = f"{len(vertexes)}" + "\n" + " ".join(map(str, vertexes))
    return describe_componenta

def dfs(graph, vertex, visited):
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            dfs(graph, v, visited)

def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Построение компоненты связности
    describe_componenta = find_componenta(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(describe_componenta))


if __name__ == "__main__":
    main()
