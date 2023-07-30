import random

from src.domain.domain import Complex
from src.repository.binary_file_repo import BinaryFileRepository
from src.repository.repository import Repository
from src.ui.console import Console
from src.services.services import Services
from src.repository.file_repository import TextfileRepository


def run(console: Console):
    while True:
        console.print_menu()
        cmd = console.get_command()
        console.do_command(cmd)


def startup(repo: Repository):
    numbers = []
    for i in range(10):
        real = random.randint(1, 99)
        img = random.randint(1, 99)
        comp = Complex(real, img)
        numbers.append(comp)
    repo.update(numbers)


# complex_repository = Repository()
# startup(complex_repository)
# complex_repository = BinaryFileRepository("binary_repo")
complex_repository = TextfileRepository("repo")
complex_service = Services(complex_repository)
complex_console = Console(complex_service)

run(complex_console)
