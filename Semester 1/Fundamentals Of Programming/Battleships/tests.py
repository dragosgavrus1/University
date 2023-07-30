import unittest

from repository import Board
from service import Service


class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.service = Service(self.board)

    def test_add_ship(self):
        pos = 'A0A1A2'
        self.service.place_ship(pos)
        player_board = self.service.list_player_board()
        self.assertEqual(player_board[0][0], '+')

        self.assertRaises(IndexError, self.service.place_ship, pos)

    def test_multiple_add(self):
        pos = 'B0B1B2'
        self.service.place_ship(pos)
        pos1 = 'C0C1C2'
        self.service.place_ship(pos1)
        pos2 = 'F0F1F2'
        self.service.place_ship(pos2)
        player_board = self.service.list_player_board()
        self.assertEqual(player_board[0][5], '+')
        self.assertNotEqual(player_board[0][1], '+')


class RepoTests(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_add_ship(self):
        self.board.place_ship(0, 0, 0, 1, 0, 2)
        board = self.board.player_board
        self.assertEqual(board[0][0], '+')

    def test_add_multiple(self):
        self.board.place_ship(1, 1, 2, 1, 3, 1)
        self.board.place_ship(0, 5, 1, 5, 2, 5)
        self.board.place_ship(0, 0, 0, 1, 0, 2)
        board = self.board.player_board
        self.assertEqual(board[0][0], '+')
        self.assertNotEqual(board[1][1], '+')
