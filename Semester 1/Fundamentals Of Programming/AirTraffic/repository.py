from datetime import datetime
from dataclasses import dataclass

from domain import Flight


@dataclass
class FlightRepo:
    all_flights = {}
    file_name: str

    def save(self, flight):
        if self.find_by_id(flight.id) is not None:
            raise ValueError("Duplicate ID")
        if self.find_by_departure_time(flight.dep_time, flight.departure) is not None:
            raise ValueError("There is already a flight at the departure time")
        if self.find_by_arrival_time(flight.arr_time, flight.arrival) is not None:
            raise ValueError("There is already a flight at the arrival time")
        self.all_flights[flight.id] = flight

    def find_all(self):
        return list(self.all_flights.values())

    def find_by_id(self, flight_id):
        if flight_id in self.all_flights:
            return self.all_flights[flight_id]
        return None

    def find_by_departure_time(self, departure_time, departure_city):
        for flight in self.find_all():
            if flight.dep_time == departure_time and flight.departure == departure_city:
                return flight
            if flight.arr_time == departure_time and flight.arrival == departure_city:
                return flight
        return None

    def find_by_arrival_time(self, arrival_time, arrival_city):
        for flight in self.find_all():
            if flight.arr_time == arrival_time and flight.arrival == arrival_city:
                return flight
            if flight.dep_time == arrival_time and flight.departure == arrival_city:
                return flight
        return None

    def delete_by_id(self, flight_id):
        if self.find_by_id(flight_id) is None:
            raise ValueError("Flight does not exist")
        del self.all_flights[flight_id]

    def read_from_file(self):
        with(open(self.file_name, "r")) as f:
            data = f.read()
            data = data.strip()
            data = data.split('\n')

        for line in data:
            line = line.strip()
            line = line.split(',')
            id = line[0]
            departure = line[1]
            # departure_time = line[2].split(':')
            departure_time = datetime.strptime(line[2], "%H:%M").time()
            arrival = line[3]
            # arrival_time = line[4].split(':')
            arrival_time = datetime.strptime(line[4], "%H:%M").time()

            self.all_flights[id] = Flight(id, departure, departure_time, arrival, arrival_time)

        f.close()

    def write_to_file(self):
        all_flights = self.find_all()
        with(open(self.file_name, "w")) as f:
            for flight in all_flights:
                f.write(flight.to_str() + '\n')

        f.close()
