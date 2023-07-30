from src.repository.repository import Repository
from src.domain.domain import Complex


class TextfileRepository(Repository):
    def __init__(self, filename):
        Repository.__init__(self)
        self.__filename = filename
        self.__read_file_data_to_list()

    def __write_to_file(self):
        with open(self.__filename, "w") as f:
            for comp in self._number_list:
                f.write("\n" + str(comp.real) + "+" + str(comp.img) + "i")
        f.close()

    def __read_file_data_to_list(self):
        with open(self.__filename, "r") as f:
            f.seek(0)
            text_lines = f.read().strip().split("\n")

        for line in text_lines:
            arr = line.strip("i")
            arr = arr.split("+")
            num = Complex(int(arr[0]), int(arr[1]))
            super().add(num)
        f.close()

    def __append_number(self, comp: Complex):
        """
        Appends to the text file the new number
        :param comp: the complex entity
        :return:
        """
        with open(self.__filename, "a") as f:
            f.write("\n" + str(comp.real) + "+" + str(comp.img) + "i")

    def add(self, comp: Complex):
        """
        The add number function for the text file repo
        :param comp: the entity
        :return:
        """
        Repository.add(self, comp)
        self.__append_number(comp)

    def find_all(self):
        return Repository.find_all(self)

    def find_all_deep(self):
        return Repository.find_all_deep(self)

    def update(self, new_list):
        Repository.update(self, new_list)
        self.__write_to_file()
