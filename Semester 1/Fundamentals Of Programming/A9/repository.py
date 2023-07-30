import numpy as np


class Board:
    def __init__(self):
        self.board = [[" " for _ in range(7)] for _ in range(6)]

    def save_move(self, row, col, value):
        self.board[row][col] = value

    def load_board(self, matrix):
        self.board = matrix

    def return_board(self):
        return self.board
