#!/usr/bin/python3
"""
N Queens Solution - Places N non-attacking queens on an NxN chessboard
"""
import sys


def is_valid_position(board, row, col):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board: List representing queen positions
        row: Current row to check
        col: Current column to check

    Returns:
        Boolean indicating if the position is valid
    """
    for i in range(col):
        if (board[i] == row or
                board[i] - i == row - col or
                board[i] + i == row + col):
            return False
    return True


def solve_nqueens(N):
    """
    Find all solutions for placing N queens on an NxN chessboard

    Args:
        N: Size of the chessboard and number of queens

    Returns:
        List of solutions where each solution is a list of [row, col] positions
    """
    solutions = []
    board = [-1] * N

    def place_queen(col):
        """
        Recursively try placing queens column by column

        Args:
            col: Current column to place queen
        """
        if col >= N:
            # Found a solution, convert board state to required format
            solution = [[i, board[i]] for i in range(N)]
            solutions.append(solution)
            return

        for row in range(N):
            if is_valid_position(board, row, col):
                board[col] = row
                place_queen(col + 1)

    place_queen(0)
    return solutions


def main():
    """
    Main function to handle input validation and execute the solution
    """
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

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
