#!/usr/bin/python3
"""
This module solves the N-queens puzzle challenge.

The challenge is to place N non-attacking queens on an N x N chessboard.
"""

import sys


def print_usage_and_exit():
    """Print the usage statement and exit with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def parse_arguments():
    """Validate and parse command line arguments."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    This only needs to check previous rows because we place queens row by row.
    """
    for i in range(row):
        # Check column conflict and diagonal conflicts
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Use backtracking to find all possible placements of queens."""
    if row == n:
        # Format the solution as a list of [row, col] pairs
        formatted_solution = [[i, board[i]] for i in range(n)]
        solutions.append(formatted_solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            # Backtrack implicitly happens on the next iteration of the loop


def main():
    """Main entry point of the program."""
    n = parse_arguments()
    board = [0] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
