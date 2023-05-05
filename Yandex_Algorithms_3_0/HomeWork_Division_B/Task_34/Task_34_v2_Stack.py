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
    for v1, v2 in set(edges):
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
    vertex_linkes = {}
    for v in graph:
        vertex_linkes[v] = len(graph[v])
    vertexes = []
    for v in range(1, n + 1):
        if visited[v] == 0:
            if v in graph:
                none_cycle = dfs_stack(graph, v, visited, vertexes)
                if not none_cycle:
                    return "-1"
            # vertexes.append(v)
            visited[v] = 2
    vertexes.reverse()
    return " ".join(map(str, vertexes))

# # Слишком глубокие рекурсии не проходят в питоне
# def dfs(graph, vertex, visited, vertexes):
#     none_cycle = True
#     for v in graph[vertex]:
#         if visited[v] == 0:
#             visited[v] = 1
#             if v in graph:
#                 none_cycle = dfs(graph, v, visited, vertexes)
#             visited[v] = 2
#             vertexes.append(v)
#         elif visited[v] == 1:
#             none_cycle = False
#         if not none_cycle:
#             return none_cycle
#     return none_cycle


# Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
def dfs_stack(graph, vertex, visited, vertexes):
    stack = [vertex]
    select_v = vertex
    visited[vertex] = 1
    while len(stack) > 0:
        select_v = stack[-1]
        print(f"pre stack: {stack}")
        print(f"pre visited: {visited}")

        # visited[select_v] = 1
        print(f"select_v: {select_v}")
        # visited[select_v] = 2
        # if visited[select_v] == 1:
        #     # vertexes.append(select_v)
        #     visited[select_v] = 2
        if select_v in graph:
            print(f"select_v: {select_v}")
            for vv in graph[select_v]:
                if visited[vv] == 0:
                    visited[vv] = 1
                    stack.append(vv)
                # elif visited[vv] == 1:
                #     return False
        print(f"pre post stack: {stack}")
        print(f"pre post visited: {visited}")
        # visited[vertex] = 1
        # select_v = stack.pop()
        if stack[-1] == select_v and visited[select_v] == 1:
            # vertexes.append(select_v)
            visited[select_v] = 2
        if visited[stack[-1]] == 2:
            select_v = stack.pop()
            vertexes.append(select_v)
        # else:
        #     select_v = stack[-1]
        # if visited[select_v] == 1:
        #     vertexes.append(select_v)
        #     visited[select_v] = 2
        print(f"post stack: {stack}")
        print(f"post visited: {visited}")
    return True

# # Слишком глубокие рекурсии не проходят в питоне, поэтому dfs реализован на стеке
# def dfs_stack(graph, vertex, visited, vertexes):
#     stack = [vertex]
#     while len(stack) > 0:
#         print(f"pre stack: {stack}")
#         select_v = stack.pop()
#         # visited[select_v] = 1
#         print(f"select_v: {select_v}")
#         # visited[select_v] = 2
#         if visited[select_v] == 1:
#             vertexes.append(select_v)
#             visited[select_v] = 2
#         if select_v in graph:
#             print(f"select_v: {select_v}")
#             for vv in graph[select_v]:
#                 if visited[vv] == 0:
#                     visited[vv] = 1
#                     stack.append(vv)
#                 elif visited[vv] == 1:
#                     return False
#         print(f"post stack: {stack}")
#     return True

def main():
    # считываем входные данные
    n, m, edges = load_data(INPUT_FILE)
    # Топологическая сортировка
    sorted_graph = topology_sort(n, m, edges)
    # Записываем результат в output.txt
    save_output(OUTPUT_FILE, str(sorted_graph))


if __name__ == "__main__":
    main()
