import unittest

from src.repository import Board
from src.service import Service


class TickTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.service = Service(self.board)

    def test_blinker_tick(self):
        self.service.place_pattern(1, 1, 0)
        self.service.tick()
        board = self.service.list_board()
        self.assertNotEqual(board[1][1], 'X')

    def test_beacon_tick(self):
        self.service.place_pattern(1, 1, 3)
        self.service.tick()
        board = self.service.list_board()
        self.assertNotEqual(board[2][2], 'X')

    def tearDown(self):
        board = [[' ' for _ in range(8)] for _ in range(8)]
        self.board.update_board(board)
