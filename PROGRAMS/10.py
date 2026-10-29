import heapq

def astar(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node == goal:
            print("Shortest Path:", path)
            print("Total Cost:", g)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(queue,
                                   (new_f, new_g, neighbor,
                                    path + [neighbor]))

    print("Path not found")

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 7, 'B': 6, 'C': 5,
    'D': 2, 'E': 4, 'F': 2, 'G': 0
}

astar(graph, heuristic, 'A', 'G')
