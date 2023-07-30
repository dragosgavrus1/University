from service import GameLogic


class UI:
    def __init__(self, game_logic: GameLogic):
        self.game_logic = game_logic

    def get_command(self):
        try:
            column = int(input("Move: "))
            if column > 6 or column < -1:
                raise IndexError("Column should be between 0 and 6")
            return column
        except ValueError:
            raise ValueError("Column should be integer")

    def display_board(self):
        print("  0  1  2  3  4  5  6 ")
        board = self.game_logic.list_board()
        for row in range(6):
            for col in range(7):
                print("|", end="")
                if board[row][col] == "X":
                    print("🔴", end="")
                if board[row][col] == "O":
                    print("🔵", end="")
                if board[row][col] == " ":
                    print("  ", end="")
            print("|")

    def play(self, col):
        self.game_logic.make_move(col)
        self.winner()
        self.is_draw()
        self.game_logic.make_ai_move()
        self.winner()
        self.is_draw()

    def is_draw(self):
        if self.game_logic.check_draw() is True:
            self.display_board()
            print("    It is a Draw!")
            exit()

    def winner(self):
        if self.game_logic.check_winner() != " ":
            if self.game_logic.check_winner() == "X":
                self.display_board()
                print("    Player Won!")
                exit()
            elif self.game_logic.check_winner() == "O":
                self.display_board()
                print("    Computer Won!")
                exit()
