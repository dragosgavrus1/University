import random

from src.domain.domain import Book
from src.repository.book_repository import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, book):
        """
        Adds a book to the repository
        :param book: the book entity
        :return:
        """
        self.book_repository.save(book)

    def remove_book(self, book_id):
        """
        Removes a book by the given id
        :param book_id: the id of the book to be deleted
        :return:
        """
        self.book_repository.delete_by_id(book_id)

    def update_book(self, book_id, title, author):
        """
        Updateing a book's information
        :param book_id: the book's id
        :param title: the new title
        :param author: the new author
        :return:
        """
        book = Book(book_id, title, author)
        self.book_repository.update(book)

    def list_books(self):
        return self.book_repository.find_all()

    def search_book_id(self, query):
        query = str(query).lower()
        matches = []
        all_books = self.book_repository.find_all()
        for book in all_books:
            if query in str(book.book_id).lower():
                matches.append(book)
        return matches

    def search_book_title(self, query):
        query = query.lower()
        matches = []
        all_books = self.book_repository.find_all()
        for book in all_books:
            if query in book.title.lower():
                matches.append(book)
        return matches

    def search_book_author(self, query):
        query = query.lower()
        matches = []
        all_books = self.book_repository.find_all()
        for book in all_books:
            if query in book.author.lower():
                matches.append(book)
        return matches

    def set_up(self):
        for i in range(10):
            titles = ['Title 1', 'Title 2', 'Title 3', 'Title 4', 'Title 5', 'To kill a mockingbird', 'Ion', 'Moby Dick', 'Morometii', 'The Great Gatsby', 'The Catcher in the Rye']
            authors = ['Author 1', 'Author 2', 'Herman Melville', 'Liviu Rebreanu', 'Harper Lee', 'F. Scott Fitzgerald', 'Marin Preda','J.D. Salinger','Emil Cioran']
            book_id = random.randint(1, 200)
            title = random.choice(titles)
            author = random.choice(authors)
            book = Book(book_id, title, author)
            self.add_book(book)
