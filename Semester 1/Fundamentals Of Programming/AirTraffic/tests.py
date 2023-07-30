import unittest

from domain import Flight
from repository import FlightRepo


class RepoTests(unittest.TestCase):
    def setUp(self):
        self.flight_repo = FlightRepo("")

    def test_add(self):
        flight = Flight('AA100', 'Loc1', '13:00', 'Loc2', '14:00')
        self.flight_repo.save(flight)
        all_flights = self.flight_repo.find_all()
        self.assertIn(flight, all_flights)

    def test_add_duplicate_id(self):
        flight = Flight('AA100', 'Loc1', '13:00', 'Loc2', '14:00')
        self.assertRaises(ValueError, self.flight_repo.save, flight)

    