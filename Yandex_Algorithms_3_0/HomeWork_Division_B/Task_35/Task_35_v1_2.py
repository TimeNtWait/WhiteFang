# https://contest.yandex.ru/contest/45468/problems/35/
# Дивизион  B
# 35. Поиск цикла
from sys import setrecursionlimit

# Снимаем ограничеи на кол-во рекурсий
setrecursionlimit(200000)
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


# Читаем данные из input.txt
def load_data(filename):
    with open(filename, "r") as file:
        n = int(file.readline())
        graph_matrix = []
        for _ in range(n):
            graph_matrix.append(list(map(int, file.readline().split())))
    return n, graph_matrix


# Записываем результат в output.txt
def save_output(filename, result_data):
    with open(filename, "w") as file:
        file.write(result_data)


# Формируем граф из матрицы смежности
def create_orient_graph(n, graph_matrix):
    graph = {}
    for i in range(n):
        for j in range(n):
            if graph_matrix[i][j] != 0:
                v1 = i + 1
                v2 = j + 1
                if v1 in graph:
                    graph[v1].append(v2)
                else:
                    graph[v1] = [v2]
    return graph


# Поиск цикла в графе
def find_cycle(n, graph_matrix):
    '''
    входные данные
    :n — количество вершин в графе
    :graph_matrix — матрица смежности

    выходные данные
    :cycle_info - Инфомрация о найденых циклах в графе
    '''
    graph = create_orient_graph(n, graph_matrix)
    # print(f"graph:{graph}")
    visited = {}
    for v in range(1, n + 1):
        visited[v] = 0
    vertexes = []
    for v in range(1, n + 1):
        if visited[v] == 0:
            if v in graph:
                cycle_vertex = dfs(graph, v, visited, vertexes, 0)
                if cycle_vertex != []:
                    # print(cycle_vertex)
                    cycle_path = [cycle_vertex[-1]]
                    for i in range(len(cycle_vertex) - 2, -1, -1):
                        if cycle_vertex[i] != cycle_vertex[-1]:
                            cycle_path.append(cycle_vertex[i])
                        else:
                            break
                    # cycle_path.reverse()
                    # print(f"visited: {visited}")
                    cycle_info = "YES\n" + str(len(cycle_path)) + "\n" + " ".join(map(str, cycle_path))
                    return cycle_info
            vertexes.append(v)
            visited[v] = 2
    return "NO"


# Слишком глубокие рекурсии не проходят в питоне
def dfs(graph, vertex, visited, vertexes, parent):
    for v in graph[vertex]:
        if visited[v] == 0:
            visited[v] = 1
            vertexes.append(v)
            cycle_vertex = dfs(graph, v, visited, vertexes, vertex)
            visited[v] = 2
            if cycle_vertex != []:
                return cycle_vertex
        elif visited[v] == 1 and v != parent:
            vertexes.append(v)
            return vertexes
    return []


def main():
    # считываем входные данные
    n, graph_matrix = load_data(INPUT_FILE)
    # Поиск цикла в графе
    cycle_info = find_cycle(n, graph_matrix)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(cycle_info))


if __name__ == "__main__":
    main()
