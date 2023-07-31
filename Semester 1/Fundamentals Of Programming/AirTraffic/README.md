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
