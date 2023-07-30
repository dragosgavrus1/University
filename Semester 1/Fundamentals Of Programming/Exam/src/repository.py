class Board:
    def __init__(self):
        self.__board = [[' ' for _ in range(8)] for _ in range(8)]

    def return_board(self):
        return self.__board

    def save_board(self, filename):
        try:
            with open(filename, 'w') as f:
                board = self.__board
                for i in range(8):
                    for j in range(8):
                        f.write(board[i][j] + ',')

                    f.write('\n')
            f.close()
        except Exception:
            raise Exception

    def load_board(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.read()
                lines = lines.split('\n')
                for i in range(8):
                    line = lines[i]
                    line = line.split(',')
                    for j in range(8):
                        self.__board[i][j] = line[j]
        except Exception:
            raise Exception

    def update_board(self, board):
        self.__board = board

    def add_to_board(self, board):
        for i in range(8):
            for j in range(8):
                if self.__board[i][j] == 'X' or board[i][j] == 'X':
                    self.__board[i][j] = 'X'
