def bfs(graph, s, t, parent):
    """
    Пошук в ширину для знаходження шляху між s та t.
    """
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]

def ford_fulkerson(graph, source, sink):
    """
    Функція, що знаходить максимальний потік з вершини source до вершини sink у графі graph.
    """
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

# Зчитуємо матрицю з файлу
with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    graph = []
    for i in range(n):
        row = list(map(int, f.readline().strip().split()))
        graph.append(row)

# Запускаємо алгоритм Форда-Фалкерсона
source, sink = 0, n-1
max_flow = ford_fulkerson(graph, source, sink)
print("Максимальний потік: ", max_flow)
