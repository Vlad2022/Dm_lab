# Відкриємо файл та зчитаємо дані
with open('input.txt', 'r') as file:
    data = file.read().split('\n')
    n = int(data[0]) # кількість вершин графа
    graph = [] # масив для зберігання матриці ваг
    for i in range(1, n+1):
        row = list(map(int, data[i].split()))
        graph.append(row)

# Початкові значення для алгоритму Пріма
visited = [0] * n
visited[0] = 1
edges = []

# Запускаємо алгоритм Пріма
for i in range(n - 1):
    min_edge = [None, None, float('inf')] # [вершина1, вершина2, вага]
    for j in range(n):
        if visited[j] == 1:
            for k in range(n):
                if visited[k] == 0 and graph[j][k]:
                    if graph[j][k] < min_edge[2]:
                        min_edge = [j, k, graph[j][k]]
    visited[min_edge[1]] = 1
    edges.append(min_edge)

# Виведемо результат
print('Ребра остовного дерева:')
for edge in edges:
    print(f'{edge[0]} - {edge[1]}, вага: {edge[2]}')
