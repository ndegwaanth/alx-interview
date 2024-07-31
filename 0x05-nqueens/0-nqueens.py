#!/usr/bin/python3
"""N-Queen"""
import sys


def print_solution(board):
    """Prints the board in the required format"""
    result = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                result.append([row, col])
    print(result)


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]"""
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    """Solves the N-Queens problem using backtracking"""
    if row == len(board):
        print_solution(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1)
            board[row][col] = '.'  # Backtrack
    return False


def main():
    """Main function to handle input and start the solving process"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
