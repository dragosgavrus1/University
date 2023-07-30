import pickle

from src.repository.repository import Repository
from src.domain.domain import Complex


class BinaryFileRepository(Repository):
    def __init__(self, filename):
        Repository.__init__(self)
        self.__filename = filename

    def __read_from_binary_file(self):
        try:
            with open(self.__filename, "rb") as f:
                self._number_list = pickle.load(f)
        except EOFError:
            self._number_list = []

    def __write_to_binary_file(self):
        with open(self.__filename, "wb") as f:
            pickle.dump(self._number_list, f)

    def add(self, comp: Complex):
        """
        Adds the new number to the list and writes it in the file
        :param comp: the complex number
        :return:
        """
        self.__read_from_binary_file()
        Repository.add(self, comp)
        self.__write_to_binary_file()

    def find_all(self):
        self.__read_from_binary_file()
        return Repository.find_all(self)

    def update(self, new_list):
        Repository.update(self, new_list)
        self.__write_to_binary_file()


