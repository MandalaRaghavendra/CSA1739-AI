from collections import deque

def solve_puzzle(start, goal):
    queue = deque([(start, [])])
    visited = {tuple(start)}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print("Solution found:")
            for step in path + [state]:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            return

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for move in moves:
            new_state = state[:]
            new_state[zero], new_state[move] = (
                new_state[move], new_state[zero]
            )

            key = tuple(new_state)
            if key not in visited:
                visited.add(key)
                queue.append((new_state, path + [state]))

    print("No solution found.")

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

solve_puzzle(start, goal)
