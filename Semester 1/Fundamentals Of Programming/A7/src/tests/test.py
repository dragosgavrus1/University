from src.domain.domain import Complex
from src.services.services import Services
from src.repository.repository import Repository
from unittest import TestCase

class Test(TestCase):
    def setUp(self):
        self.__repo = Repository()
        self.__service = Services(self.__repo)


    def test_add(self):
        self.__service.add_number(1,2)
        self.assertEqual(len(self.__repo.find_all()),11)

    # def test_add():
    #     """
    #     Test function for the add functionality
    #     :return:
    #     """
    #     num1 = Complex(1, 2)
    #     repo = Repository()
    #     repo.add(num1)
    #     list1 = repo.find_all()
    #     assert num1 == list1