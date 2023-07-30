import unittest

from repository import Board
from service import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game_logic = GameLogic(self.board)

    def test_check_winner(self):
        # test horizontal win
        board = [["X", "X", "X", "X", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]
        self.board.load_board(board)
        self.assertEqual(self.game_logic.check_winner(), "X")

        # test vertical win
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 ["X", " ", " ", " ", " ", " ", " "],
                 ["X", " ", " ", " ", " ", " ", " "],
                 ["X", " ", " ", " ", " ", " ", " "],
                 ["X", " ", " ", " ", " ", " ", " "]]
        self.board.load_board(board)
        self.assertEqual(self.game_logic.check_winner(), "X")

        # test diagonal win
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", "X", " "],
                 [" ", " ", " ", " ", "X", " ", " "],
                 [" ", " ", " ", "X", " ", " ", " "],
                 [" ", " ", "X", " ", " ", " ", " "]]
        self.board.load_board(board)
        self.assertEqual(self.game_logic.check_winner(), "X")

    def test_check_draw(self):
        # test no draw
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]
        self.board.load_board(board)
        self.assertFalse(self.game_logic.check_draw())

        # test draw
        board = [["O", "X", "O", "X", "O", "X", "O"],
                 ["O", "X", "O", "X", "O", "X", "0"],
                 ["X", "O", "X", "O", "X", "O", "X"],
                 ["X", "O", "X", "O", "X", "O", "X"],
                 ["O", "X", "O", "X", "O", "X", "0"],
                 ["O", "X", "O", "X", "O", "X", "0"]]
        self.board.load_board(board)
        self.assertTrue(self.game_logic.check_draw())

    def test_make_move(self):
        # test valid move
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]
        move = 0
        self.board.load_board(board)
        self.assertTrue(self.game_logic.make_move(move))

        # test invalid move
        board = [["X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "X", "X", "X"]]
        move = 0
        self.board.load_board(board)
        # self.assertRaises(self.game_logic.make_move(move), IndexError)
        self.assertRaises(IndexError, self.game_logic.make_move(move), 0)
        # self.assertRaises(IndexError)

    def test_ai_move(self):
        # test AI move
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "]]
        self.board.load_board(board)
        move = self.game_logic.ai_move()
        self.assertTrue(0 <= move <= 6)


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board_test = Board()

    def test_save_move(self):
        self.board_test.save_move(0, 5, "X")
        board = self.board_test.return_board()
        self.assertEqual(board[0][5], "X")

    def test_return_board(self):
        self.board_test.save_move(0, 5, "X")
        board = self.board_test.return_board()
        self.assertEqual(board[0][5], "X")

    def test_load_board(self):
        board = [[" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 [" ", " ", " ", " ", " ", " ", " "],
                 ["X", " ", " ", " ", " ", " ", " "]]
        self.board_test.load_board(board)
        board2 = self.board_test.return_board()
        self.assertEqual(board2[5][0], "X")
