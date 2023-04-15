import numpy as np
from heapq import heappush, heappop


class Node:
    def __init__(self, level, path, bound):
        self.level = level
        self.path = path
        self.bound = bound

    def __lt__(self, other):
        return self.bound < other.bound


def tsp(dist_matrix):
    n = dist_matrix.shape[0]
    unvisited = set(range(1, n))
    curr_node = 0
    tour = [0]

    while unvisited:
        next_node = min(unvisited, key=lambda x: dist_matrix[curr_node][x])
        tour.append(next_node)
        unvisited.remove(next_node)
        curr_node = next_node

    tour.append(0)
    tour_cost = sum(dist_matrix[tour[i], tour[i + 1]] for i in range(n))
    return tour, tour_cost


def bound(path, dist_matrix):
    """
    Обчислює верхню межу для шляху.
    """
    cost = 0
    for i in range(len(path) - 1):
        cost += dist_matrix[path[i], path[i + 1]]
    if len(path) == dist_matrix.shape[0]:
        cost += dist_matrix[path[-1], path[0]]
    else:
        cost += np.min(dist_matrix[path[-1], [x for x in range(dist_matrix.shape[0]) if x not in path]])
    return cost


def solve_tsp(dist_matrix):
    n = dist_matrix.shape[0]
    heap = []
    # Додаємо вузол з кореневим шляхом [0] та верхньою межею вартості найкоротшого шляху, який проходить через 0.
    heappush(heap, Node(level=1, path=[0], bound=bound([0], dist_matrix)))
    min_tour = None
    min_cost = float('inf')

    while heap:
        node = heappop(heap)
        if node.bound < min_cost:
            for i in range(1, n):
                if i not in node.path:
                    child_path = node.path + [i]
                    child_bound = bound(child_path, dist_matrix)
                    if child_bound < min_cost:
                        child_node = Node(level=node.level + 1, path=child_path, bound=child_bound)
                        if len(child_path) == n:
                            tour_cost = sum(dist_matrix[child_path[i], child_path[i + 1]] for i in range(n - 1)) + \
                                        dist_matrix[child_path[-1], child_path[0]]
                            if tour_cost < min_cost:
                                min_cost = tour_cost
                                min_tour = child_path + [0]
                        else:
                            heappush(heap, child_node)
    return min_tour, min_cost


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        dist_matrix = np.zeros((n, n))

        for i in range(n):
            row = f.readline().strip().split()
            for j in range(n):
                dist_matrix[i, j] = int(row[j])

    # Виводимо результат методу "найближчого сусіда"
    tour, tour_cost = tsp(dist_matrix)
    print("Шлях, знайдений методом найближчого сусіда: ", tour)
    print("Вартість шляху, знайденого методом найближчого сусіда: ", tour_cost)

    # Виводимо результат методу "гілки і межі"
    min_tour, min_cost = solve_tsp(dist_matrix)
    print("Шлях, знайдений методом гілок і меж: ", min_tour)
    print("Вартість шляху, знайденого методом гілок і меж: ", min_cost)
