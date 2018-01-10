from ai import AI
from domain import Board
from menu import UI
from service import BoardService

board = Board()
board_service = BoardService(board)
ai = AI(board)
ui = UI(board_service, ai)
ui.menu()
