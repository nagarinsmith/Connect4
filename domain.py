class Board:
    def __init__(self):
        """
        Initialises the board as a 7x6 array
        """
        self.__board = [[0 for y in range(6)] for x in range(7)]

    def get_position(self, x, y):
        """
        Returns the specified position on the board
        :param x: Position on the x axis
        :param y: Position on the y axis
        :return: The (x, y) position
        """
        return self.__board[x][y]

    def set_position(self, x, y, piece):

        """
        Sets the specified position with a specified value
        :param x: Position on the x axis
        :param y: Position on the y axis
        :param piece: Value of the position
        :return: None
        """
        self.__board[x][y] = piece
