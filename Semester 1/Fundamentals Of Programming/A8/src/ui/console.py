from src.domain.domain import Book, Client, Rental
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from src.test.exceptions import IdException, CommandException


class UI:
    def __init__(self, book_service: BookService, client_service: ClientService, rental_service: RentalService):
        self.book_service = book_service
        self.client_service = client_service
        self.rental_service = rental_service

    def menu(self):
        print("1. Book operations")
        print("2. Client operations")
        print("3. Print rents")
        print("4. Rent a book")
        print("5. Return a book")
        print("6. Most rented books")
        print("7. Most active clients")
        print("8. Most rented author")
        print("0. Exit")
        print("")

    def print_options(self):
        print("1. Add")
        print("2. Remove")
        print("3. Update")
        print("4. Show")
        print("5. Search by id")
        print("6. Search by title")
        print("7. Search by author")
        print("")

    def print_options2(self):
        print("1. Add")
        print("2. Remove")
        print("3. Update")
        print("4. Show")
        print("5. Search by id")
        print("6. Search by name")
        print("")

    def add_book(self):
        """
        Adds a new book to the book repository trough book service
        :return:
        """
        try:
            book_id = int(input("Book id: "))
            if book_id < 0:
                raise IdException("Id should be positive")
            title = input("Title: ")
            author = input("Author: ")
            book = Book(book_id, title, author)
            self.book_service.add_book(book)
        except ValueError:
            raise IdException("Id must be an integer")

    def add_client(self):
        """
        Adds a new client to the client repository trough client service
        :return:
        """
        try:
            client_id = int(input("Client id: "))
            if client_id < 0:
                raise IdException("Id should be positive")
            name = input("Name: ")
            client = Client(client_id, name)
            self.client_service.add_client(client)
        except ValueError:
            raise IdException("Id must be an integer")

    def remove_book(self):
        """
        Removes a book from the repository
        :return:
        """
        try:
            book_id = int(input("Book id: "))
            self.book_service.remove_book(book_id)
        except ValueError:
            raise IdException("Id must be an integer")

    def remove_client(self):
        """
        Removes a client from the repository
        :return:
        """
        try:
            client_id = int(input("Client id: "))
            self.client_service.remove_client(client_id)
        except ValueError:
            raise IdException("Id must be an integer")

    def update_book(self):
        """        Updates a book's information in the repo
        :return:
        """
        try:
            book_id = int(input("Book id: "))
            title = input("New title: ")
            author = input("New author: ")
            self.book_service.update_book(book_id, title, author)
        except ValueError:
            raise IdException("Id must be an integer")

    def update_client(self):
        """
        Updates a client's information in the repo
        :return:
        """
        try:
            client_id = int(input("Client id: "))
            name = input("New name: ")
            self.client_service.update_client(client_id,name)
        except ValueError:
            raise IdException("Id must be an integer")

    def print_books(self):
        books = self.book_service.list_books()
        for book in books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def print_clients(self):
        clients = self.client_service.list_clients()
        for client in clients:
            print(f"Client ID: {client.client_id}, Name: {client.name}")

    def print_rents(self):
        rents = self.rental_service.list_all()
        for rent in rents:
            print(f"Rental id: {rent.rental_id}, Book id: {rent.book_id}, Client id: {rent.client_id}, Rented date: {rent.rented_date}, Returned date: {rent.returned_date}")

    def rent_book(self):
        try:
            book_id = int(input("Book id: "))
            client_id = int(input("Client id: "))
            self.rental_service.rent_book(book_id, client_id)
        except ValueError:
            raise IdException("Id must be an integer")

    def return_book(self):
        try:
            rental_id = int(input("Rental id: "))
            self.rental_service.return_book(rental_id)
        except ValueError:
            raise IdException("Id must be an integer")

    def search_book_id(self):
        try:
            id = int(input("Id: "))
            matches = self.book_service.search_book_id(id)
            for book in matches:
                print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
        except ValueError:
            raise IdException("Id must be an integer")

    def search_book_title(self):
        title = input("Title: ")
        matches = self.book_service.search_book_title(title)
        for book in matches:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def search_book_author(self):
        author = input("Author: ")
        matches = self.book_service.search_book_author(author)
        for book in matches:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def search_client_id(self):
        try:
            id = int(input("Id: "))
            matches = self.client_service.search_client_id(id)
            for client in matches:
                print(f"Client ID: {client.client_id}, Name: {client.name}")
        except ValueError:
            raise IdException("Id must be an integer")

    def search_client_name(self):
        name = input("Name: ")
        matches = self.client_service.search_client_name(name)
        for book in matches:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

    def most_rented_books(self):
        most_rented = self.rental_service.most_rented_books()
        for book_id, title, author, count in most_rented:
            print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Rented {count} times")

    def most_active_clients(self):
        most_active = self.rental_service.most_active_clients()
        for client_id, name, days in most_active:
            print(f"Client ID: {client_id}, Name: {name}, Rented {days} days")

    def most_rented_author(self):
        sorted_authors = self.rental_service.most_rented_authors()
        for author, count in sorted_authors:
            print(f"Author {author} was rented {count} times")

    def get_command(self):
        try:
            cmd = int(input("Command: "))
            return cmd
        except ValueError:
            raise CommandException("Command must be an integer")

    def do_command(self, cmd):
        if cmd == 0:
            exit()
        if cmd == 1:
            self.print_options()
            cmd2 = self.get_command()
            if cmd2 == 1:
                self.add_book()
            if cmd2 == 2:
                self.remove_book()
            if cmd2 == 3:
                self.update_book()
            if cmd2 == 4:
                self.print_books()
            if cmd2 == 5:
                self.search_book_id()
            if cmd2 == 6:
                self.search_book_title()
            if cmd2 == 7:
                self.search_book_author()

        if cmd == 2:
            self.print_options2()
            cmd2 = self.get_command()
            if cmd2 == 1:
                self.add_client()
            if cmd2 == 2:
                self.remove_client()
            if cmd2 == 3:
                self.update_client()
            if cmd2 == 4:
                self.print_clients()
            if cmd2 == 5:
                self.search_client_id()
            if cmd2 == 6:
                self.search_client_name()

        if cmd == 3:
            self.print_rents()

        if cmd == 4:
            self.rent_book()

        if cmd == 5:
            self.return_book()

        if cmd == 6:
            self.most_rented_books()

        if cmd == 7:
            self.most_active_clients()

        if cmd == 8:
            self.most_rented_author()
