from repository import FlightRepo
from service import Service
from ui import UI

repo = FlightRepo('FlightData')
fligt_service = Service(repo)
flight_ui = UI(fligt_service)

repo.read_from_file()

while True:
    flight_ui.print_menu()
    flight_ui.run()

