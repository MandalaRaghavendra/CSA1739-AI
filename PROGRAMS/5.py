
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)

moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def valid(m, c):
    return 0 <= m <= 3 and 0 <= c <= 3 and (
        m == 0 or m >= c
    ) and (
        3 - m == 0 or 3 - m >= 3 - c
    )

queue = deque([(start, [])])
visited = set()

while queue:
    state, path = queue.popleft()

    if state in visited:
        continue
    visited.add(state)

    if state == goal:
        print("Solution:")
        for step in path + [state]:
            print(step)
        break

    m, c, boat = state

    for dm, dc in moves:
        if boat == 1:
            new_state = (m - dm, c - dc, 0)
        else:
            new_state = (m + dm, c + dc, 1)

        if valid(new_state[0], new_state[1]):
            if new_state not in visited:
                queue.append((new_state, path + [state]))
