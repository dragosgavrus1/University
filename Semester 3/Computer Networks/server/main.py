import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen(2)

players = []
player_symbols = ['X', 'O']
board = [' ' for _ in range(9)]
current_player = 0  # Player 1 starts


def make_board_str():
    return '\n' + board[0] + '|' + board[1] + '|' + board[2] + '\n' + '-+-+-' + '\n' + board[3] + '|' + board[4] + '|' + \
           board[5] + '\n' + '-+-+-' + '\n' + board[6] + '|' + board[7] + '|' + board[8] + '\n '


def print_board():
    print()
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])


while len(players) < 2:
    client_socket, addr = server.accept()
    print(f"Connected to {addr}")

    player_num = len(players)
    players.append(client_socket)
    client_socket.send(f"You are Player {player_num + 1}\n".encode())

for player_socket in players:
    player_socket.send("Both players are connected. The game is starting!\n".encode())

while True:
    player_socket = players[current_player]
    player_socket.send("Your turn. Send the position (0-8) where you want to place your symbol.\n".encode())
    data = player_socket.recv(1024).decode()

    try:
        position = int(data)
        if 0 <= position < 9 and board[position] == ' ':
            board[position] = player_symbols[current_player]
            print_board()

            # Check for a win or a draw
            if (board[0] == board[1] == board[2] and board[0] != ' ' or
                    board[3] == board[4] == board[5] and board[3] != ' ' or
                    board[6] == board[7] == board[8] and board[6] != ' ' or
                    board[0] == board[3] == board[6] and board[0] != ' ' or
                    board[1] == board[4] == board[7] and board[1] != ' ' or
                    board[2] == board[5] == board[8] and board[2] != ' ' or
                    board[0] == board[4] == board[8] and board[0] != ' ' or
                    board[2] == board[4] == board[6] and board[2] != ' '):
                for player in players:
                    player.send(f"Player {current_player + 1} wins!".encode())
                print(f"Player {current_player + 1} wins!")
                break
            elif ' ' not in board:
                for player in players:
                    player.send("It's a draw!\n".encode())
                print("It's a draw!")
                break
            player_socket.send(str.encode(make_board_str()))
            current_player = 1 - current_player
            players[current_player].send(str.encode(make_board_str()))
        else:
            player_socket.send("Invalid move. Try again.\n".encode())
    except ValueError:
        player_socket.send("Invalid input. Send a number (0-8).\n".encode())

for player_socket in players:
    player_socket.close()
