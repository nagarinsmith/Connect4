from random import randint


class AI:
    """
    Ai class, currently gives a random position, where is available
    """
    def __init__(self, board):
        self.__board = board

    def generator(self):
        x = randint(0, 6)
        while self.__board.get_position(x, 5) != 0:
            x = randint(0, 6)
        return x
