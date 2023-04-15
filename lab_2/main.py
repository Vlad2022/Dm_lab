import itertools
import numpy as np

# Зчитуємо матрицю відстаней з файлу
with open('input.txt') as f:
    n = int(f.readline())
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        distance_matrix[i] = np.array(list(map(int, f.readline().split())))

# Знаходимо всі можливі комбінації міст
cities = range(n)
routes = list(itertools.permutations(cities))

# Знаходимо маршрут з найменшою відстанню
min_distance = np.inf
best_route = None
for route in routes:
    distance = 0
    for i in range(n-1):
        distance += distance_matrix[route[i], route[i+1]]
    distance += distance_matrix[route[-1], route[0]]
    if distance < min_distance:
        min_distance = distance
        best_route = route

# Виводимо маршрут та відстань
print(f"Найкращій шлях: {best_route}")
print(f"Відстань: {min_distance}")