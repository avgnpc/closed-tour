import time
import random

def is_valid_move(board, n, row, col):
    return 0 <= row < n and 0 <= col < n and board[row][col] == -1

def print_solution(board):
    for row in board:
        print(row)
    print("\n")

def knight_tour(n, start_row, start_col, timeout):
    board = [[-1 for _ in range(n)] for _ in range(n)]

    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    start_time = time.time()

    def is_timeout():
        return time.time() - start_time > timeout

    def calculate_warnsdorff_priority(row, col):
        count = 0
        for i, j in moves:
            new_row, new_col = row + i, col + j
            if is_valid_move(board, n, new_row, new_col):
                for x, y in moves:
                    if is_valid_move(board, n, new_row + x, new_col + y):
                        count += 1
        return count

    def knight_tour_recursive(row, col, move_number):
        board[row][col] = move_number

        if move_number == n * n - 1:
            if (start_row, start_col) in [(row + i, col + j) for i, j in moves]:
                print_solution(board)
                return True
        elif not is_timeout():
            possible_moves = [(calculate_warnsdorff_priority(row + i, col + j), (row + i, col + j)) for i, j in moves]
            possible_moves.sort(key=lambda x: x[0] + random.random())  # Randomize the order of moves

            for _, (new_row, new_col) in possible_moves:
                if is_valid_move(board, n, new_row, new_col):
                    if knight_tour_recursive(new_row, new_col, move_number + 1):
                        return True

        board[row][col] = -1
        return False

    return knight_tour_recursive(start_row, start_col, 0)

try:
    start_row = int(input("Enter the starting row (0 to 7): "))
    start_col = int(input("Enter the starting column (0 to 7): "))
    if not (0 <= start_row <= 7 and 0 <= start_col <= 7):
        raise ValueError("Invalid starting position.")
except ValueError as e:
    print(f"Error: {e}. Please enter valid integers.")
else:
    while not knight_tour(8, start_row, start_col, timeout=0.003):
        pass
