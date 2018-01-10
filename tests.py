from unittest import TestCase
from unittest.mock import patch

from ai import AI
from domain import Board
from exceptions import ServiceException, MenuException
from menu import UI
from service import BoardService


class Tests(TestCase):
    def test_board_domain(self):
        board = Board()
        for x in range(7):
            for y in range(6):
                self.assertEqual(board.get_position(x, y), 0,
                                 "Board is not initialised with 0, error is located at: %s, %s" % (x, y))
        board.set_position(1, 0, 1)
        self.assertEqual(board.get_position(1, 0), 1, "set_position not working for Board")

    def test_board_service_add_piece_and_exceptions(self):
        board = Board()
        board_service = BoardService(board)
        self.assertEqual(board_service.show,
                         '0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n0 0 0 0 0 0 0 \n',
                         "This shouldn't not work anymore")
        board_service.add_piece(1, 1)
        self.assertEqual(board.get_position(1, 0), 1, "add_piece not working")
        # Testing column full exception
        board_service.add_piece(1, 1)
        board_service.add_piece(1, 1)
        board_service.add_piece(1, 1)
        board_service.add_piece(1, 1)
        board_service.add_piece(1, 1)
        self.assertRaises(ServiceException, lambda: board_service.add_piece(1, 1))

    def test_full_board(self):
        board = Board()
        board_service = BoardService(board)
        for x in range(7):
            for y in range(6):
                board.set_position(x, y, 1)
        self.assertEqual(board_service.game_state(), 0)

    def test_x_axis(self):
        board = Board()
        board_service = BoardService(board)
        for x in range(1, 5):
            board_service.add_piece(x, 1)
        self.assertEqual(board_service.game_state(), 1)

    def test_y_axis(self):
        board = Board()
        board_service = BoardService(board)
        for y in range(1, 5):
            board_service.add_piece(1, 1)
        self.assertEqual(board_service.game_state(), 1)

    def test_diagonal(self):
        board = Board()
        board_service = BoardService(board)
        board.set_position(0, 0, 1)
        board.set_position(1, 1, 1)
        board.set_position(2, 2, 1)
        board.set_position(3, 3, 1)
        self.assertEqual(board_service.game_state(), 1)
        board.set_position(2, 2, 0)
        board.set_position(6, 0, 1)
        board.set_position(5, 1, 1)
        board.set_position(4, 2, 1)
        board.set_position(3, 3, 1)
        self.assertEqual(board_service.game_state(), 1)

    def test_menu_exception(self):
        board = Board()
        board_service = BoardService(board)
        ai = AI(board)
        ui = UI(board_service, ai)
        with patch('builtins.input', side_effect='0'):
            self.assertRaises(MenuException, lambda: ui.menu())

    def test_ai(self):
        board = Board()
        ai = AI(board)
        board.set_position(0, 5, 1)
        board.set_position(1, 5, 1)
        board.set_position(2, 5, 1)
        board.set_position(3, 5, 1)
        board.set_position(4, 5, 1)
        board.set_position(5, 5, 1)
        self.assertIsInstance(ai.generator(), int)
