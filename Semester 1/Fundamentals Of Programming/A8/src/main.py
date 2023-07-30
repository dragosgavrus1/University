from src.repository.book_repository import BookRepository
from src.repository.client_repository import ClientRepository
from src.repository.rental_repository import RentalRepository
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from src.test.exceptions import IdException, CommandException
from src.ui.console import UI


def run(console: UI):
    while True:
        try:
            console.menu()
            cmd = console.get_command()
            console.do_command(cmd)
        except IdException as e:
            print("Id Exception ", e.message)
        except CommandException as e:
            print("Command Exception ", e.message)


book_repo = BookRepository()
book_service = BookService(book_repo)
client_repo = ClientRepository()
client_service = ClientService(client_repo)
rental_repo = RentalRepository()
rental_service = RentalService(rental_repo, book_repo, client_repo)
console = UI(book_service, client_service, rental_service)

book_service.set_up()
client_service.set_up()
run(console)
