from repository import Board
from service import GameLogic
from ui import UI

board = Board()
game_logic = GameLogic(board)
ui = UI(game_logic)

board1 = [[" ", "X", "O", "X", "O", "X", "O"],
          ["O", "X", "O", "X", "O", "X", "0"],
          ["X", "O", "X", "O", "X", "O", "X"],
          ["X", "O", "X", "O", "X", "O", "X"],
          ["O", "X", "O", "X", "O", "X", "0"],
          ["O", "X", "O", "X", "O", "X", "0"]]


# board.load_board(board1)


# ui.display_board()

def play_game():
    while True:
        try:
            ui.display_board()
            col = ui.get_command()
            ui.play(col)
        except ValueError as err:
            print(err)
        except IndexError as err:
            print(err)


if __name__ == "__main__":
    play_game()
    ui.display_board()
