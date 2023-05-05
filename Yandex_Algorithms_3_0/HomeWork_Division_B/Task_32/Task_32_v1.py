# https://contest.yandex.ru/contest/45468/problems/32/
# Дивизион  B
# 32. Компоненты связности
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
    :describe_components - информация о компоненте связности: количество вершин + Вершины компоненты связности,
    перечисленные в порядке возрастания номеров.
    '''
    if n == 0:
        return "0"
    elif m == 0:
        # print([f"1\n{i+1}" for i in range(n)])
        return f"{n}\n" + '\n'.join(map(str, [f"1\n{i+1}" for i in range(n)]))

    graph = create_graph(edges)
    visited = {}
    for v in range(1, n+1):
        visited[v] = False
    comp = 1
    vertex_component = {}
    for v in range(1, n+1):
        if not visited[v]:
            vertexes = []
            if v in graph:
                dfs(graph, v, visited, vertexes)
            else:
                vertexes.append(v)
            vertex_component[comp] = vertexes
            comp += 1
    describe_components = f"{len(vertex_component.keys())}\n"
    for key in vertex_component.keys():
        describe_components += f"{len(vertex_component[key])}\n"
        describe_components += ' '.join(map(str,sorted(vertex_component[key]))) + "\n"
    return describe_components

def dfs(graph, vertex, visited, vertexes):
    for v in graph[vertex]:
        if not visited[v]:
            visited[v] = True
            vertexes.append(v)
            dfs(graph, v, visited, vertexes)

def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Построение компоненты связности
    describe_componenta = find_componenta(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(describe_componenta))


if __name__ == "__main__":
    main()
