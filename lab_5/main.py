import networkx as nx

# функція для перевірки ізоморфізму двох графів
def is_isomorphic(G1, G2):
    return nx.is_isomorphic(G1, G2)

# функція для знаходження графа, на якому ізоморфізм не встановлюється
def find_non_isomorphic_graph(G1, G2):
    # створюємо копію графа G1
    G = G1.copy()
    # проходимо по кожній парі зв’язків (u1, v1) та (u2, v2) з двох графів
    for u1, v1 in G1.edges():
        for u2, v2 in G2.edges():
            # перевіряємо, чи можна замінити зв’язки
            if not G.has_edge(u1, v1) and not G.has_edge(u2, v2):
                G.add_edge(u1, v1)
                G.remove_edge(u1, u2)
                G.add_edge(u2, v2)
                # якщо ізоморфізм не встановлюється, повертаємо граф G
                if not is_isomorphic(G, G2):
                    return G
                # відновлюємо початковий стан графа G
                G.remove_edge(u2, v2)
                G.add_edge(u1, u2)
                G.remove_edge(u1, v1)
    # якщо ізоморфізм встановлюється, повертаємо граф, ідентичний G1
    return G1

# створюємо два графи
G1 = nx.Graph()
G1.add_edges_from([(1,2), (2,3), (3,4), (4,1)])
G2 = nx.Graph()
G2.add_edges_from([(5,6), (6,7), (7,8), (8,5)])

# перевіряємо, чи ізоморфні графи G1 та G2
if is_isomorphic(G1, G2):
    print("Графи ізоморфні")
else:
    print("Графи неізоморфні")

G = find_non_isomorphic_graph(G1, G2)

print("Граф G1:")
print(G1.edges())
print("Граф G2:")
print(G2.edges())
print("Граф, на якому ізоморфізм не встановлюється:")
print(G.edges())

if is_isomorphic(G1, G):
    print("Графи ізоморфні")
else:
    print("Графи неізоморфні")