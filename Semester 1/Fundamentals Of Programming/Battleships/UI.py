from service import Service


class UI:
    def __init__(self, service: Service):
        self.service = service

    @staticmethod
    def get_command():
        cmd = input('Command: ')
        return cmd

    def place_ship(self, positions):
        """
        Calls the service function which places a ship if the command is valid and displays the updated board
        :param positions: the positions for the ship
        :return:
        """
        self.service.place_ship(positions)
        self.display_board()

    def game_start(self):
        self.service.place_ai_ships()
        self.play_game()

    def play_game(self):
        while self.service.game_end() is not True:
            self.display_board()
            self.display_hidden_ai_board()
            cmd = self.get_command()
            cmd = cmd.lower()
            cmd = cmd.split()
            if cmd[0] == 'attack':
                self.attack(cmd[1])
                self.ai_attack()
            elif cmd[0] == 'cheats':
                self.display_ai_board()
            else:
                print('incorrect input for attack')

        self.game_won()

    def game_won(self):
        if self.service.ai_lives == 0:
            self.display_board()
            self.display_hidden_ai_board()
            print("Player won!")
        elif self.service.player_lives == 0:
            self.display_board()
            self.display_hidden_ai_board()
            print("Computer won!")

    def attack(self, cell):
        if self.service.player_attack(cell):
            print("Player hit!")
        else:
            print('Player missed!')

    def ai_attack(self):
        if self.service.ai_attack():
            print("Computer hit!")
        else:
            print('Computer missed!')

    def run_command(self):
        cmd = self.get_command()
        cmd = cmd.lower()
        cmd = cmd.split()
        if cmd[0] == 'ship':
            self.place_ship(cmd[1])
        elif cmd[0] == 'start':
            if self.service.game_can_start():
                self.game_start()
            else:
                print('You need to place 2 ships before the game can start')
        elif cmd[0] == 'cheats':
            self.display_ai_board()
        elif cmd[0] == 'exit':
            exit()
        else:
            print('Incorrect input')

    def display_board(self):
        board = self.service.list_player_board()
        print('   Player Board')
        print('   A B C D E F')
        for x in range(6):
            print(x, end=' ')
            for y in range(6):
                print(board[x][y], end=" ")
            print(" ")
        print('')

    def display_ai_board(self):
        board = self.service.list_targeting_board()
        print(' Targeting Board')
        print('   A B C D E F')
        for x in range(6):
            print(x, end=' ')
            for y in range(6):
                print(board[x][y], end=" ")
            print(" ")
        print('')

    def display_hidden_ai_board(self):
        board = self.service.list_targeting_board()
        print('     Cheats ')
        print('   A B C D E F')
        for x in range(6):
            print(x, end=' ')
            for y in range(6):
                if board[x][y] != '+':
                    print(board[x][y], end=" ")
                else:
                    print('.', end=' ')
            print(" ")
        print('')
