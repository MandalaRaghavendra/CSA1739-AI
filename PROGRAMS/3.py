from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Target achieved!")
            return

        queue.extend([
            (capacity1, y),
            (x, capacity2),
            (0, y),
            (x, 0),
            (x - min(x, capacity2 - y), y + min(x, capacity2 - y)),
            (x + min(y, capacity1 - x), y - min(y, capacity1 - x))
        ])

    print("Target cannot be achieved.")

water_jug(4, 3, 2)
