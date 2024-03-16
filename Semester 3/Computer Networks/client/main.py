import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)

        if "The game is starting" in data:
            break

    while True:
        data = client.recv(1024).decode('utf-8')
        print(data)

        if "Your turn" in data:
            position = input("Enter your move (0-8): ")
            client.send(position.encode('utf-8'))

        if "wins!" in data or "It's a draw" in data:
            break

    client.close()
