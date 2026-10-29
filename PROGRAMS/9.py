from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    for path in permutations(cities):
        route = [start] + list(path) + [start]
        cost = sum(graph[route[i]][route[i + 1]]
                   for i in range(n))

        if cost < min_cost:
            min_cost = cost
            best_path = route

    print("Shortest Path:", best_path)
    print("Minimum Cost:", min_cost)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(graph, 0)
