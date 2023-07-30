"""



"""
from src.Ui import UI
from src.repository import Board
from src.service import Service

board = Board()
service = Service(board)
ui = UI(service)

if __name__ == '__main__':
    while True:
        try:
            ui.display_board()
            ui.do_command()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)