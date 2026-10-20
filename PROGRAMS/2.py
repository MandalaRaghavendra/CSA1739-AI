def solve_n_queens(board, row):
    if row == 8:
        for r in board:
            print(" ".join("Q" if x else "." for x in r))
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0

    return False


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1),
                     range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1),
                     range(col + 1, 8)):
        if board[i][j] == 1:
            return False

    return True


board = [[0] * 8 for _ in range(8)]

if not solve_n_queens(board, 0):
    print("No solution exists")
