from dataclasses import dataclass
from datetime import datetime, time, timedelta

from repository import FlightRepo


@dataclass
class Service:
    flight_repo: FlightRepo

    def add_flight(self, flight):
        self.flight_repo.save(flight)
        self.flight_repo.write_to_file()

    def delete(self, id):
        self.flight_repo.delete_by_id(id)
        self.flight_repo.write_to_file()

    def list_all(self):
        return self.flight_repo.find_all()

    def most_active_airports(self):
        most_active = {}
        all_flights = self.list_all()
        for flight in all_flights:
            if flight.departure not in most_active:
                most_active[flight.departure] = 1
            else:
                most_active[flight.departure] += 1

            if flight.arrival not in most_active:
                most_active[flight.arrival] = 1
            else:
                most_active[flight.arrival] += 1

        most_active = sorted(most_active.items(), key=lambda x: x[1], reverse=True)

        return most_active

    def no_flights(self):
        all_flights = self.list_all()
        day_start = time(0, 0)
        day_end = time(23, 59)
        latest_arrival = day_start

        all_flights = sorted(all_flights, key=lambda x: x.dep_time)

        open_time = []

        for flight in all_flights:
            if latest_arrival < flight.dep_time:
                open_time.append([latest_arrival, flight.dep_time])
                latest_arrival = flight.arr_time
            elif latest_arrival < flight.arr_time:
                latest_arrival = flight.arr_time

        if latest_arrival < day_end:
            open_time.append([latest_arrival, day_end])

        datetime_open_time = [(datetime.combine(datetime.today().date(), x[0]), datetime.combine(datetime.today().date(), x[1])) for x in open_time]

        open_time = sorted(datetime_open_time, key=lambda x: (x[1] - x[0]).seconds, reverse=True)

        open_time = [(x[0].time(), x[1].time()) for x in open_time]

        return open_time

    def backup_radar(self):
        all_flights = self.list_all()
        day_start = time(0, 0)
        last_arrival = day_start

        all_flights = sorted(all_flights, key=lambda x: x.arr_time)

        most_flights = []
        for flight in all_flights:
            if flight.dep_time > last_arrival:
                most_flights.append(flight)
                last_arrival = flight.arr_time

        return most_flights
