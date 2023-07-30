from datetime import datetime


class Flight:
    def __init__(self, id, departure, dep_time, arrival, arr_time):
        self.__id = id
        self.__departure = departure
        self.__dep_time: datetime = dep_time
        self.__arrival = arrival
        self.__arr_time: datetime = arr_time

    @property
    def id(self):
        return self.__id

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value

    @property
    def dep_time(self):
        return self.__dep_time

    @dep_time.setter
    def dep_time(self, value):
        self.__dep_time = value

    @property
    def arrival(self):
        return self.__arrival

    @arrival.setter
    def arrival(self, value):
        self.__arrival = value

    @property
    def arr_time(self):
        return self.__arr_time

    @arr_time.setter
    def arr_time(self, value):
        self.__arr_time = value

    def __str__(self):
        hour = "{:02d}".format(self.dep_time.hour)
        minute = "{:02d}".format(self.dep_time.minute)
        arr_hour = "{:02d}".format(self.arr_time.hour)
        arr_minute = "{:02d}".format(self.arr_time.minute)
        return f'{self.id},{self.departure},{hour}:{minute},{self.arrival},{arr_hour}:{arr_minute} '

    def to_str(self):
        hour = "{:02d}".format(self.dep_time.hour)
        minute = "{:02d}".format(self.dep_time.minute)
        arr_hour = "{:02d}".format(self.arr_time.hour)
        arr_minute = "{:02d}".format(self.arr_time.minute)
        return f'{self.id},{self.departure},{hour}:{minute},{self.arrival},{arr_hour}:{arr_minute} '
