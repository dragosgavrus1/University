import copy

from src.domain.domain import Complex


class Repository:
    def __init__(self):
        self._number_list = []

    def add(self, comp: Complex):
        """
        Adds the complex entity to the list
        :param comp: the complpex number
        :return:
        """
        self._number_list.append(comp)

    def find_all(self):
        return self._number_list

    def find_all_deep(self):
        return copy.deepcopy(self._number_list)

    def update(self, new_list):
        self._number_list = new_list

