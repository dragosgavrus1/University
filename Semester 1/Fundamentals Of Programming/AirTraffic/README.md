Air Traffic Control
Write a console-based application to help air traffic control (ATC) monitor all domestic flights taking place during one day (00:00 – 23:59). The application must include the following features:
Flight information is kept in a text file, using the format in the example below. When the program starts, flight information is read from the file [1p]. Each modification is persisted to the text file [1p].
Add a new flight. Each flight has an identifier, a departure city and time, and an arrival city and time [1p]. Flight identifiers are unique; flight times are between 15 and 90 minutes; an airport can handle a single operation (departure or arrival) during each minute [1p].
Delete a flight. The user provides the flight identifier. If it does not exist, an error message is displayed [1p].
List the airports, in decreasing order of activity (number of departures and arrivals during the day) [1p].
List the time intervals during which no flights are taking place, in decreasing order of length. [1.5p].
The tracking radar suffers a failure. The backup radar can be used, but it can only track a single flight at a time. Determine the maximum number of flights that can proceed as planned. List them using the format below [1.5p]:
05:45 | 06:40 | RO650 | Cluj - Bucuresti

Non-functional requirements:
Implement an object-oriented, layered architecture solution using the Python language.
Provide specification and unit tests for Repository/Controller functions related with the second functionality. In case specification or tests are missing, the functionality is graded at 50%.

Observations!
The day starts at 00:00 and ends at 23:59.
Default 1p.

Example input file.
RO650,Cluj,05:45,Bucuresti,06:40
0B3302,Cluj,07:15,Bucuresti,08:15
SLD322,Timisoara,09:05,Cluj,10:00
RO643,Bucuresti,10:15,Cluj,11:10
RO734,Timisoara,10:45,Iasi,12:25
KL2710,Timisoara,14:25,Bucuresti,15:40
RO745,Cluj,12:50,Iasi,14:05
RO746,Iasi,14:30,Cluj,15:50
RO647,Bucuresti,18:05,Cluj,19:00
KL2706,Bucuresti,18:10,Timisoara,19:05
RO733,Iasi,08:30,Timisoara,10:20
SLD363,Cluj,19:35,Timisoara,20:30
RO649,Bucuresti,21:55,Cluj,22:50
0B3101,Bucuresti,22:55,Cluj,23:55
RP621,Bucuresti,07:30,Oradea,08:55
RO622,Oradea,09:20,Bucuresti,10:40
RO627,Bucuresti,17:55,Oradea,19:20
RO628,Oradea,19:45,Bucuresti,21:05
XL897,TgMures,08:55,Oradea,09:30
XL898,Oradea,20:45,TgMures,21:25
LH012,Iasi,14:35,Oradea,15:35
LH013,Oradea,17:00,Iasi,18:10


