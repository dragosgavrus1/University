class Board:
    def __init__(self):
        self.player_board = [['.' for _ in range(6)] for _ in range(6)]
        self.targeting_board = [['.' for _ in range(6)] for _ in range(6)]
        self.ships = []

    def place_ship(self, x1, y1, x2, y2, x3, y3):
        """
        Places a ship at these coordinates which are separated in service
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param x3:
        :param y3:
        :return: changes the player board
        """
        if len(self.ships) == 2:        # if there are already 2 ships deletes the first one
            first_ship = self.ships.pop(0)
            self.delete_ship(first_ship[0], first_ship[1], first_ship[2], first_ship[3], first_ship[4],
                             first_ship[5])
        self.player_board[x1][y1] = '+'
        self.player_board[x2][y2] = '+'
        self.player_board[x3][y3] = '+'
        self.ships.append([x1, y1, x2, y2, x3, y3]) # adds current last ship to ships list

    def delete_ship(self, x1, y1, x2, y2, x3, y3):
        self.player_board[x1][y1] = '.'
        self.player_board[x2][y2] = '.'
        self.player_board[x3][y3] = '.'

    def hit_player(self, x, y):
        if self.player_board[x][y] == '+':
            self.player_board[x][y] = 'X'
            return True
        else:
            self.player_board[x][y] = 'O'
            return False

    def hit_ai(self, x, y):
        if self.targeting_board[x][y] == '+':
            self.targeting_board[x][y] = 'X'
            return True
        else:
            self.targeting_board[x][y] = 'O'
            return False

    def place_ai_ships(self, row, col, row2, col2):
        self.targeting_board[row][col] = '+'  # horizontal ship
        self.targeting_board[row][col + 1] = '+'
        self.targeting_board[row][col + 2] = '+'

        self.targeting_board[row2][col2] = '+'  # vertical ship
        self.targeting_board[row2 + 1][col2] = '+'
        self.targeting_board[row2 + 2][col2] = '+'

    def return_board(self):
        return self.player_board

    def return_targeting(self):
        return self.targeting_board
