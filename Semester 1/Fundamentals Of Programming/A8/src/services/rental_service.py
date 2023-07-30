from src.domain.domain import Rental
from src.repository.book_repository import BookRepository
from src.repository.client_repository import ClientRepository
from src.repository.rental_repository import RentalRepository

from datetime import date

from src.test.exceptions import CommandException


class RentalService:
    def __init__(self, rental_repository: RentalRepository, book_repository: BookRepository, client_repository: ClientRepository):
        self.rental_repository = rental_repository
        self.book_repository = book_repository
        self.client_repository = client_repository

    def check_available(self, book_id):
        rentals = self.rental_repository.find_all()
        for rental in rentals:
            if rental.book_id == book_id:
                if rental.returned_date is None:
                    return False
        return True

    def rent_book(self, book_id, client_id):
        if self.check_available(book_id) is False:
            raise CommandException("Book is not available")
        else:
            today = date.today()
            rental = Rental(self.rental_repository.rental_id, book_id, client_id, today.day, None)
            self.rental_repository.add_rental(rental)

    def return_book(self, rental_id):
        all_rentals = self.rental_repository.find_all()
        found = False
        for rental in all_rentals:
            if rental.rental_id == rental_id:
                found = True
                today = date.today()
                if rental.returned_date is not None:
                    raise CommandException("Book is already returned")
                rental.returned_date = today.day
                self.rental_repository.update(rental)
        if found is False:
            raise CommandException("Rental does not exist")

    def most_rented_books(self):
        rentals_count = {}
        all_rentals = self.rental_repository.find_all()
        for rental in all_rentals:
            if rental.book_id not in rentals_count:
                rentals_count[rental.book_id] = 1
            else:
                rentals_count[rental.book_id] += 1
        sorted_books = sorted(rentals_count.items(), key=lambda x: x[1], reverse=True)

        all_books = self.book_repository.find_all()
        most_rented = []
        for book_id, count in sorted_books:
            for book in all_books:
                if book.book_id == book_id:
                    most_rented.append((book.book_id, book.title, book.author, count))
                    break
        return most_rented

    def most_active_clients(self):
        rental_days = {}
        all_rentals = self.rental_repository.find_all()
        for rental in all_rentals:
            if rental.client_id not in rental_days:
                rental_days[rental.client_id] = 0
            if rental.returned_date is not None:
                rental_days[rental.client_id] += (rental.returned_date - rental.rented_date + 1)

        sorted_clients = sorted(rental_days.items(), key=lambda x: x[1], reverse=True)

        all_clients = self.client_repository.find_all()
        most_active = []
        for client_id, days in sorted_clients:
            for client in all_clients:
                if client.client_id == client_id:
                    most_active.append((client.client_id, client.name, days))
        return most_active

    def most_rented_authors(self):
        rentals_count = {}
        all_rentals = self.rental_repository.find_all()
        all_books = self.book_repository.find_all()
        for rental in all_rentals:
            for book in all_books:
                if book.book_id == rental.book_id:
                    if book.author not in rentals_count:
                        rentals_count[book.author] = 1
                    else:
                        rentals_count[book.author] += 1
                        break

        sorted_authors = sorted(rentals_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_authors

    def list_all(self):
        return self.rental_repository.find_all()
