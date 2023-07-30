import random

from src.domain.domain import Client
from src.repository.client_repository import ClientRepository


class ClientService:
    def __init__(self, client_repository: ClientRepository):
        self.client_repository = client_repository

    def add_client(self, client):
        """
        Adds a client to the repo
        :param client: the client
        :return:
        """
        self.client_repository.save(client)

    def remove_client(self, client_id):
        """
        Removes a client by the given id
        :param client_id: the id of the client to be removed
        :return:
        """
        self.client_repository.delete_by_id(client_id)

    def update_client(self, client_id, name):
        """
        Update a client information
        :param client_id: the client id
        :param name: the new name
        :return:
        """
        client = Client(client_id, name)
        self.client_repository.update(client)

    def list_clients(self):
        return self.client_repository.find_all()

    def search_client_id(self, query):
        query = str(query).lower()
        matches = []
        all_clients = self.client_repository.find_all()
        for client in all_clients:
            if query in str(client.client_id).lower():
                matches.append(client)
        return matches

    def search_client_name(self, query):
        query = query.lower()
        matches = []
        all_clients = self.client_repository.find_all()
        for client in all_clients:
            if query in client.name.lower():
                matches.append(client)
        return matches

    def set_up(self):
        for i in range(10):
            names = ['Dorian', 'Andrei', 'Alex', 'Andrew', 'Briana', 'Adriana', 'Charles', 'Leo', 'Tudor', 'Jane', 'Cristian', 'Raphael', 'Radu']
            client_id = random.randint(1, 200)
            name = random.choice(names)
            client = Client(client_id, name)
            self.add_client(client)
