from UI import UI
from repository import Board
from service import Service

board = Board()
service = Service(board)
ui = UI(service)

while True:
    # ui.display_board()
    try:
        ui.run_command()
    except Exception as e:
        print(e)
