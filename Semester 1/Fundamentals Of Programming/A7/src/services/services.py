import random

from src.domain.domain import Complex
from src.repository.repository import Repository
from random import randint


class Services:
    def __init__(self, repository):
        self.repository = repository
        self.history = []

    def add_number(self, real, img):
        """
        Add a number to the repository
        :param real: the real part
        :param img: the imaginary part
        :return:
        """
        self.history.append(self.repository.find_all_deep())
        number = Complex(real, img)
        self.repository.add(number)

    def display_list(self):
        return self.repository.find_all()

    def filter(self, start, end):
        self.history.append(self.repository.find_all())
        all_numbers = self.repository.find_all()
        all_numbers = all_numbers[start:end + 1]
        self.repository.update(all_numbers)

    def undo(self):
        if len(self.history) == 0:
            raise ValueError("No more undos")
        self.repository.update(self.history.pop())


def test_add():
    """
    Test function for the add functionality
    :return:
    """
    list2 = []
    num1 = Complex(1, 2)
    repo = Repository()
    repo.add(num1)
    list2.append(num1)
    list1 = repo.find_all()
    assert len(list1) == len(list2)


def test_service_add():
    list1 = []
    num1 = Complex(1, 2)
    repo = Repository()
    service = Services(repo)
    service.add_number(1, 2)
    list1.append(num1)
    list2 = repo.find_all()
    assert len(list1) == len(list2)


def test_create():
    num1 = Complex(1, 2)
    x = num1.real
    y = num1.img
    assert x == 1 and y == 2


test_add()
test_create()
test_service_add()
