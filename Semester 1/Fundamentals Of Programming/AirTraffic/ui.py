from dataclasses import dataclass
from datetime import datetime

from domain import Flight
from service import Service


@dataclass
class UI:
    flight_service: Service

    def add_flight(self):
        try:
            id = input('Id: ')
            departure = input('Departure city: ')
            departure_time = input('Departure time: ')
            arrival = input('Arrival city: ')
            arrival_time = input('Arrival time: ')

            departure_time = datetime.strptime(departure_time, "%H:%M")
            arrival_time = datetime.strptime(arrival_time, "%H:%M")
            diff_time = arrival_time - departure_time
            if diff_time.seconds / 60 > 90 or diff_time.seconds / 60 < 15:
                raise Exception("Flight time is incorrect")

            departure_time = departure_time.time()
            arrival_time = arrival_time.time()
            flight = Flight(id, departure, departure_time, arrival, arrival_time)
            self.flight_service.add_flight(flight)
        except ValueError:
            print("Time is incorrect")
        except Exception as e:
            print(e)

    def delete_flight(self):
        id = input('Flight id:')
        self.flight_service.delete(id)

    def print_most_active(self):
        most_active = self.flight_service.most_active_airports()
        for airport , count in most_active:
            print(f'{airport}: {count} flights')

    def no_flights_intervals(self):
        open_time = self.flight_service.no_flights()
        for time in open_time:
            time0_hour = "{:02d}".format(time[0].hour)
            time0_minute = "{:02d}".format(time[0].minute)
            time1_hour = "{:02d}".format(time[1].hour)
            time1_minute = "{:02d}".format(time[1].minute)
            print(f'{time0_hour}:{time0_minute}, {time1_hour}:{time1_minute}')

    def broken_radar(self):
        most_flights = self.flight_service.backup_radar()
        print(f'The maximum number of flights to proceed as planned is {len(most_flights)}')
        for flight in most_flights:
            hour = "{:02d}".format(flight.dep_time.hour)
            minute = "{:02d}".format(flight.dep_time.minute)
            arr_hour = "{:02d}".format(flight.arr_time.hour)
            arr_minute = "{:02d}".format(flight.arr_time.minute)
            print(f'{hour}:{minute} | {arr_hour}:{arr_minute} | {flight.id} | {flight.departure} - {flight.arrival}')

    @staticmethod
    def print_menu():
        print("")
        print('1. List flights')
        print('2. Add flight')
        print('3. Delete a flight')
        print('4. Most active airports')
        print('5. No flights')
        print('6. Backup radar')
        print('0. Exit')
        print("")

    def print_flights(self):
        all_flights = self.flight_service.list_all()
        for flight in all_flights:
            print(flight)

    @staticmethod
    def get_command():
        try:
            cmd = int(input('Command: '))
            return cmd
        except ValueError:
            print("Command should be integer")

    def run(self):
        cmd = self.get_command()
        if cmd == 1:
            self.print_flights()
        if cmd == 2:
            self.add_flight()
        if cmd == 3:
            self.delete_flight()
        if cmd == 4:
            self.print_most_active()
        if cmd == 5:
            self.no_flights_intervals()
        if cmd == 6:
            self.broken_radar()
        if cmd == 0:
            exit()
