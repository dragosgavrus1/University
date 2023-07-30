from src.test.exceptions import IdException


class ClientRepository:
    def __init__(self):
        self.__all_clients = {}

    def find_all(self):
        return list(self.__all_clients.values())

    def save(self, client):
        """
        Adds the client to the list
        :param client: the client
        :return:
        """
        try:
            if self.__find_by_id(client.client_id) is not None:
                raise IdException("Duplicate id")
            self.__all_clients[client.client_id] = client
        except IdException as e:
            print("Id Exception", e.message)

    def __find_by_id(self, client_id):
        if client_id in self.__all_clients:
            return self.__all_clients[client_id]
        return None

    def update(self, client):
        """
        Updates a client with new information
        :param client: the new client information
        :return:
        """
        if self.__find_by_id(client.client_id) is None:
            raise IdException("Id does not exist")
        self.__all_clients[client.client_id] = client

    def delete_by_id(self, client_id):
        """
        Deletes a client through the id from the repo
        :param client_id: the id of the deleted client
        :return:
        """
        if self.__find_by_id(client_id) is None:
            raise IdException("Id does not exist")
        del self.__all_clients[client_id]
