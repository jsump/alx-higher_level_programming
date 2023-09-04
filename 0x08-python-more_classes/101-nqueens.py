#!/usr/bin/python3
import sys
"""
Module: 101-nqueens

This module is to solve the N queens puzzle.
This is the challenge of placing N non-attacking
queens on an N×N chessboard.
"""


def solve_nqueens(n):
    """
    This is to check if the user called the program
    with the wrong number of arguments.
    Prints Usage: nqueens N, followed by a new line,
    and exit with the status 1.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """
        This checks whether is is safe to place the queen in
        a partucular position on the chessboard.
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(row, n, board=None):
        """
        This tries different positions recursively for each row
        until it finds a valid solution.
        """
        if board is None:
            board = [-1] * n

        if row == n:
            print([[i, board[i]] for i in range(n)])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(row + 1, n, board)

    solve(0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be number")
        sys.exit(1)
