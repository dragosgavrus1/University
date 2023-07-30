from src.services.services import Services


class Console:
    def __init__(self, complex_service: Services):
        self.__complex_service = complex_service

    def print_all_numbers(self):
        if len(self.__complex_service.display_list()) == 0:
            print("[]")

        for number in self.__complex_service.display_list():
            print(number)

    def add_ui(self):
        try:
            real = int(input("The real part: "))
            img = int(input("The imaginary part: "))
            self.__complex_service.add_number(real, img)
        except ValueError:
            print("Values should be integers")

    def filter(self):
        try:
            start = int(input("Starting index: "))
            end = int(input("Ending index:"))
            self.__complex_service.filter(start, end)
        except ValueError:
            print("Indexes should be integers")

    def undo(self):
        try:
            self.__complex_service.undo()
        except ValueError:
            print("No more undos")

    def print_menu(self):
        print("1. Add a number")
        print("2. Show the list")
        print("3. Filter the list")
        print("4. Undo")
        print("0. Exit")
        print("")

    def get_command(self):
        cmd = int(input("Option: "))
        return cmd

    def do_command(self, cmd):
        if cmd == 0:
            exit()
        if cmd == 1:
            self.add_ui()
        if cmd == 2:
            self.print_all_numbers()
        if cmd == 3:
            self.filter()
        if cmd == 4:
            self.undo()

