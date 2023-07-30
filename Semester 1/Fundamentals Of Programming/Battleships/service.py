import random

from repository import Board


class Service:
    def __init__(self, board: Board):
        self.board = board
        self.ai_lives = 6
        self.player_lives = 6

    def place_ship(self, position: str):
        """
        Places a ship if the instructions are correct
        :param position: the string with positions
        :return: Exception if not correct
        """
        try:
            position = position.lower()
            position = position.strip()
            x1 = int(position[1])
            x2 = int(position[3])
            x3 = int(position[5])
            y1 = ord(position[0]) - ord('a')
            y2 = ord(position[2]) - ord('a')
            y3 = ord(position[4]) - ord('a')

            player_board = self.board.return_board()
            if (x1 == x2 == x3 and (y1 == y2 + 1 == y3 + 2 or y1 == y2 - 1 == y3 - 2)) or (
                    y1 == y2 == y3 and (x1 == x2 + 1 == x3 + 2 or x1 == x2 - 1 == x3 - 2)):
                if player_board[x1][y1] == '+' or player_board[x2][y2] == '+' or player_board[x3][y3] == '+':
                    raise IndexError
                self.board.place_ship(x1, y1, x2, y2, x3, y3)
            else:
                raise IndexError
        except IndexError:
            raise IndexError("Incorrect placement of the ship")
        except ValueError:
            raise ValueError("Incorrect input")

    def game_can_start(self):
        if len(self.board.ships) == 2:
            return True
        else:
            return False

    def place_ai_ships(self):
        row = random.randint(0, 5)
        col = random.randint(0, 3)
        ai_board = self.list_targeting_board()
        ai_board[row][col] = '+'
        ai_board[row][col + 1] = '+'
        ai_board[row][col + 2] = '+'

        row2 = random.randint(0, 3)
        col2 = random.randint(0, 5)
        while ai_board[row2][col2] == '+' or ai_board[row2 + 1][col2] == '+' or ai_board[row2 + 2][col2] == '+':
            row2 = random.randint(0, 3)
            col2 = random.randint(0, 5)
        self.board.place_ai_ships(row, col, row2, col2)

    def player_attack(self, cell):
        try:
            cell = cell.lower()
            x = int(cell[1])
            y = ord(cell[0]) - ord('a')
            if 0 > x or x > 5 or y < 0 or y > 5:
                raise IndexError
            if self.board.hit_ai(x, y):
                self.ai_lives -= 1
                return True
            return False
        except IndexError:
            raise IndexError('Incorrect attack coordinates')
        except ValueError:
            raise ValueError('Incorrect attack input')

    def ai_attack(self):
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        player_board = self.list_player_board()
        while player_board[x][y] == 'X' or player_board[x][y] == 'O':
            x = random.randint(0, 5)
            y = random.randint(0, 5)
        if self.board.hit_player(x, y):
            self.player_lives -= 1
            return True
        return False

    def game_end(self):
        if self.player_lives == 0 or self.ai_lives == 0:
            return True
        return False

    def list_player_board(self):
        return self.board.return_board()

    def list_targeting_board(self):
        return self.board.return_targeting()
