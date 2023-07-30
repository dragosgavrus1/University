class RentalRepository:
    def __init__(self):
        self.__all_rentals = {}
        self.rental_id = 1

    def add_rental(self, rental):
        # todo check for book,client id
        self.__all_rentals[rental.rental_id] = rental
        self.rental_id += 1

    def find_by_id(self, rental_id):
        if rental_id in self.__all_rentals:
            return self.__all_rentals[rental_id]
        return None

    def find_by_book_id(self, book_id):
        for rental in self.__all_rentals:
            if rental == book_id:
                return self.__all_rentals[rental]
        return None

    def update(self, rental):
        if self.find_by_id(rental.rental_id) is None:
            raise ValueError("Id does not exist")
        self.__all_rentals[rental.rental_id] = rental

    def find_all(self):
        return list(self.__all_rentals.values())


