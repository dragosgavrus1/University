from src.test.exceptions import IdException


class BookRepository:
    def __init__(self):
        self.__all_books = {}

    def find_all(self):
        return list(self.__all_books.values())

    def save(self, book):
        """
        Adds a new book to the repo
        :param book:
        :return:
        """
        try:
            if self.__find_by_id(book.book_id) is not None:
                raise IdException("Duplicate id")
            self.__all_books[book.book_id] = book
        except IdException as e:
            print("Id Exception", e.message)

    def __find_by_id(self, book_id):
        if book_id in self.__all_books:
            return self.__all_books[book_id]
        return None

    def update(self, book):
        """
        Updates a book
        :param book: the book entity
        :return:
        """
        if self.__find_by_id(book.book_id) is None:
            raise IdException("Id does not exist")
        self.__all_books[book.book_id] = book

    def delete_by_id(self, book_id):
        """
        Delete a book by id
        :param book_id: the id
        :return:
        """
        if self.__find_by_id(book_id) is None:
            raise IdException("Id does not exist")
        del self.__all_books[book_id]
