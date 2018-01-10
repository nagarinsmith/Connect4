from exceptions import ServiceException


class BoardService:
    """
    Links the menu with the repository and provides essential functions
    """
    def __init__(self, board):
        self.__board = board

    @property
    def show(self):
        """
        Returns user readable game board
        :return: Game board as string
        """
        board_str = ""
        for y in reversed(range(6)):
            for x in range(7):
                board_str += str(self.__board.get_position(x, y)) + ' '
            board_str += '\n'
        return board_str

    def add_piece(self, x, piece):
        """
        Adds a piece to the board
        :param x: Coord on the x axis
        :param piece: Piece value
        :return: None
        """
        for y in range(6):
            if self.__board.get_position(x, y) == 0:
                self.__board.set_position(x, y, piece)
                break
        else:
            raise ServiceException("Column full")

    def game_state(self):
        """
        Returns the current game state
        :return: 0 for draw, 1 victory
        """
        # check for draw
        keep_alive = 0
        for x in range(7):
            if self.__board.get_position(x, 5) == 0:
                keep_alive += 1
        if keep_alive == 0:
            return 0
        # check win state on x axis
        for y in range(6):
            connected = 1
            previous_piece = -1
            for x in range(6):
                if self.__board.get_position(x, y) == previous_piece:
                    connected += 1
                else:
                    if self.__board.get_position(x, y) != 0:
                        previous_piece = self.__board.get_position(x, y)
                    else:
                        previous_piece = -1
                    connected = 1
                if connected == 4:
                    return 1
        # check win state on y axis
        for x in range(7):
            connected = 1
            previous_piece = -1
            for y in range(6):
                if self.__board.get_position(x, y) == previous_piece:
                    connected += 1
                else:
                    if self.__board.get_position(x, y) != 0:
                        previous_piece = self.__board.get_position(x, y)
                    else:
                        previous_piece = -1
                    connected = 1
                if connected == 4:
                    return 1
        # check win state on diagonal
        for x in range(7):
            for y in range(5, 2, -1):
                if x - 3 >= 0:
                    if self.__board.get_position(x, y) == self.__board.get_position(x - 1,
                                                                                    y - 1) == self.__board.get_position(
                                x - 2, y - 2) == self.__board.get_position(x - 3, y - 3) and self.__board.get_position(x, y) != 0:
                        return 1
                if x + 3 <= 6:
                    if self.__board.get_position(x, y) == self.__board.get_position(x + 1,
                                                                                    y - 1) == self.__board.get_position(
                                x + 2, y - 2) == self.__board.get_position(x + 3, y - 3) and self.__board.get_position(x, y) != 0:
                        return 1
