import random

from repository import Board


class GameLogic:
    def __init__(self, board: Board):
        self.board = board

    def make_move(self, col):
        # saving a move made by a player
        board_values = self.board.return_board()
        if board_values[0][col] != " ":
            raise IndexError("Column is full")
        for i in range(5, -1, -1):
            if board_values[i][col] == " ":
                self.board.save_move(i, col, "X")
                return True

    def make_ai_move(self):
        # saving a move made by the computer
        board_values = self.board.return_board()
        while True:
            col = self.ai_move()
            for i in range(5, -1, -1):
                if board_values[i][col] == " ":
                    self.board.save_move(i, col, "O")
                    return

    def check_winner(self):
        # code to check if there is a winner
        board = self.board.return_board()

        # check for horizontal wins
        for row in board:
            for i in range(4):
                if row[i] == row[i + 1] == row[i + 2] == row[i + 3] != " ":
                    return row[i]

        # check for vertical wins
        for col in range(7):
            for row in range(3):
                if board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] != " ":
                    return board[row][col]

        # check for first diagonal wins
        for row in range(3):
            for col in range(4):
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] != " ":
                    return board[row][col]

        # check for second diagonal wins
        for row in range(3):
            for col in range(3, 7):
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3] != " ":
                    return board[row][col]
        return None

    def ai_move(self):
        # code to determine the AI's next move
        board = self.board.return_board()
        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == " " and (row == 5 or board[row + 1][col] != " "):
                    board[row][col] = "O"
                    if self.check_winner() == "O":
                        board[row][col] = " "
                        return col
                    board[row][col] = " "

        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == " " and (row == 5 or board[row + 1][col] != " "):
                    board[row][col] = "X"
                    if self.check_winner() == "X":
                        board[row][col] = " "
                        return col
                    board[row][col] = " "

        return random.randint(0, 6)

    def check_draw(self):
        # code to check if the game is a draw
        board = self.board.return_board()
        if self.check_winner() is None:
            for row in range(6):
                for col in range(7):
                    if board[row][col] == " ":
                        return False
        return True

    def list_board(self):
        # return the board
        return self.board.return_board()
