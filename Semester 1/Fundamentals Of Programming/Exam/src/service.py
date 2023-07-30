from src.repository import Board


class Service:
    def __init__(self, board: Board):
        self.__board = board

    def list_board(self):
        return self.__board.return_board()

    def pattern(self, pattern, cord):
        try:
            cord = cord.split(',')
            x = int(cord[0])
            y = int(cord[1])
            if x > 7 or x < -1 or y > 7 or y < -1:
                raise Exception('Incorrect coordinates')
            if pattern == 'blinker':
                self.place_pattern(x, y, 0)
            elif pattern == 'block':
                self.place_pattern(x, y, 1)
            elif pattern == 'beacon':
                self.place_pattern(x, y, 2)
            elif pattern == 'tub':
                self.place_pattern(x, y, 3)
            elif pattern == 'spaceship':
                self.place_pattern(x, y, 4)
            else:
                raise Exception('Incorrect pattern')
        except ValueError:
            raise ValueError('Coordinates should be integer')

    def place_pattern(self, x, y, shape_nr):
        board = self.__board.return_board()
        temp_board = [[' ' for _ in range(8)] for _ in range(8)]
        with(open('shapes', 'r')) as f:
            lines = f.read()
            lines = lines.split('\n')
            cords = lines[shape_nr].split(',')

        for i in cords:
            i = i.split(':')
            add_x = int(i[0])
            add_y = int(i[1])
            if x + add_x > 7 or y + add_y > 7:
                raise Exception('Shape out of borders')
            if board[x + add_x][y + add_y] == 'X':
                raise Exception('There is a cell in the way')
            temp_board[x + add_x][y + add_y] = 'X'

        self.__board.add_to_board(temp_board)

    def tick(self, n=1):
        """
        The function which updates the board by n ticks
        :param n: the tick number, default on 1
        :return: updates the game board
        """
        # we create a new temporary board
        new_board = [[' ' for _ in range(8)] for _ in range(8)]
        board = self.list_board()   # we get the current board

        for nr in range(n):     # the number of ticks
            for i in range(8):
                for j in range(8):
                    # the function neighbour calculates the number of neighbours for the current position
                    if board[i][j] == 'X':
                        neigh = self.neighbour(i, j)
                        if neigh < 2 or neigh > 3:      # checks if the cell dies
                            new_board[i][j] = ' '
                        if neigh == 2 or neigh == 3:       # the cell remains alive
                            new_board[i][j] = 'X'

                    if board[i][j] == ' ':          # a new cell appears if there are 3 neighbouring alive cells
                        neigh = self.neighbour(i, j)
                        if neigh == 3:
                            new_board[i][j] = 'X'

            # we update the board with the current one after one iteration
            self.__board.update_board(new_board)

    def save_to_file(self, filename):
        self.__board.save_board(filename)

    def load_board(self, filename):
        self.__board.load_board(filename)

    def neighbour(self, x, y):
        board = self.list_board()
        neigh = 0
        if x != 0 and y != 0 and x != 7 and y != 7:
            if board[x + 1][y] == 'X':
                neigh += 1
            if board[x + 1][y + 1] == 'X':
                neigh += 1
            if board[x][y + 1] == 'X':
                neigh += 1
            if board[x - 1][y] == 'X':
                neigh += 1
            if board[x - 1][y - 1] == 'X':
                neigh += 1
            if board[x - 1][y + 1] == 'X':
                neigh += 1
            if board[x][y - 1] == 'X':
                neigh += 1
            if board[x + 1][y - 1] == 'X':
                neigh += 1

        if x == 0:
            if y == 0:
                if board[x + 1][y] == 'X':
                    neigh += 1
                if board[x + 1][y + 1] == 'X':
                    neigh += 1
                if board[x][y + 1] == 'X':
                    neigh += 1
            elif y == 7:
                if board[x + 1][y] == 'X':
                    neigh += 1
                if board[x][y - 1] == 'X':
                    neigh += 1
                if board[x + 1][y - 1] == 'X':
                    neigh += 1
            else:
                if board[x + 1][y] == 'X':
                    neigh += 1
                if board[x + 1][y + 1] == 'X':
                    neigh += 1
                if board[x][y + 1] == 'X':
                    neigh += 1
                if board[x][y - 1] == 'X':
                    neigh += 1
                if board[x + 1][y - 1] == 'X':
                    neigh += 1

        if x == 7:
            if y == 0:
                if board[x - 1][y + 1] == 'X':
                    neigh += 1
                if board[x][y + 1] == 'X':
                    neigh += 1
                if board[x - 1][y] == 'X':
                    neigh += 1
            elif y == 7:
                if board[x - 1][y] == 'X':
                    neigh += 1
                if board[x - 1][y - 1] == 'X':
                    neigh += 1
                if board[x][y - 1] == 'X':
                    neigh += 1
            else:
                if board[x - 1][y - 1] == 'X':
                    neigh += 1
                if board[x][y - 1] == 'X':
                    neigh += 1
                if board[x - 1][y + 1] == 'X':
                    neigh += 1
                if board[x][y + 1] == 'X':
                    neigh += 1
                if board[x - 1][y] == 'X':
                    neigh += 1

        return neigh
