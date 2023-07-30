import unittest

from src.domain.domain import Book, Client
from src.repository.book_repository import BookRepository
from src.repository.client_repository import ClientRepository
from src.services.book_service import BookService
from src.services.client_service import ClientService


class TestBooks(unittest.TestCase):
    def setUp(self):
        self.repository = BookRepository()
        self.service = BookService(self.repository)
        self.book1 = Book(1, 'Book1', 'Author1')
        self.book2 = Book(2, 'Book2', 'Author2')
        self.service.add_book(self.book1)
        self.service.add_book(self.book2)

    def test_add_book(self):
        book3 = Book(3, 'Book3', 'Author3')
        self.service.add_book(book3)
        self.assertIn(book3, self.service.list_books())

    def test_remove(self):
        self.service.remove_book(1)
        self.assertNotIn(self.book1, self.service.list_books())

    def test_update_book(self):
        self.service.update_book(2, title='New Book2', author='New Author2')
        all_books = self.service.list_books()
        book = all_books[1]
        self.assertEqual(book.title, 'New Book2')
        self.assertEqual(book.author, 'New Author2')

    def test_add_book_repo(self):
        book3 = Book(3, 'Book3', 'Author3')
        self.repository.save(book3)
        self.assertIn(book3, self.repository.find_all())

    def test_remove_repo(self):
        self.repository.delete_by_id(1)
        self.assertNotIn(self.book1, self.repository.find_all())

    def test_update_book_repo(self):
        book = Book(2, title='New Book2', author='New Author2')
        self.repository.update(book)
        all_books = self.repository.find_all()
        book2 = all_books[1]
        self.assertEqual(book2.title, 'New Book2')
        self.assertEqual(book2.author, 'New Author2')


class TestClients(unittest.TestCase):
    def setUp(self):
        self.repository = ClientRepository()
        self.service = ClientService(self.repository)
        self.client1 = Client(1, 'Client1')
        self.client2 = Client(2, 'Client2')
        self.service.add_client(self.client1)
        self.service.add_client(self.client2)

    def test_add_client(self):
        client3 = Client(3, 'Client3')
        self.service.add_client(client3)
        self.assertIn(client3, self.service.list_clients())

    def test_remove_client(self):
        self.service.remove_client(1)
        self.assertNotIn(self.client1, self.service.list_clients())

    def test_update_client(self):
        self.service.update_client(2, name='New Client2')
        all_clients = self.service.list_clients()
        client = all_clients[1]
        self.assertEqual(client.name, 'New Client2')

    def test_add_client_repo(self):
        client3 = Client(3, 'Client3')
        self.repository.save(client3)
        self.assertIn(client3, self.repository.find_all())

    def test_remove_client_repo(self):
        self.repository.delete_by_id(1)
        self.assertNotIn(self.client1, self.repository.find_all())

    def test_update_client_repo(self):
        client2 = Client(2, name='New Client2')
        self.repository.update(client2)
        all_clients = self.repository.find_all()
        client = all_clients[1]
        self.assertEqual(client.name, 'New Client2')

