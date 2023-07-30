from prettytable import prettytable

from src.service import Service


class UI:
    def __init__(self, service: Service):
        self.__service = service

    def display_board(self):
        board = self.__service.list_board()
        table = prettytable.PrettyTable()
        table.field_names = [str(i) for i in range(8)]

        for i in range(8):
            table.add_row(board[i])

        print(table)

    @staticmethod
    def read_command():
        cmd = input('Command: ')
        return cmd

    def do_command(self):
        try:
            cmd = self.read_command()
            cmd = cmd.lower()
            cmd = cmd.split()
            if cmd[0] == 'place':
                self.__service.pattern(cmd[1], cmd[2])
            elif cmd[0] == 'tick':
                if len(cmd) == 2:
                    n = int(cmd[1])
                    self.__service.tick(n)
                else:
                    self.__service.tick()
            elif cmd[0] == 'save':
                self.__service.save_to_file(cmd[1])
            elif cmd[0] == 'load':
                self.__service.load_board(cmd[1])
            elif cmd[0] == 'exit':
                exit()
            else:
                print('Wrong command')
        except IndexError:
            print('Incorrect command')
        except ValueError:
            print('Tick nr should be integer')
