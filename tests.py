from unittest import TestCase

from domain import Board
from exceptions import ServiceException
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

    def test_board_service(self):
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
