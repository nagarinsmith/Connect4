from exceptions import MenuException


class UI:
    def __init__(self, board, ai):
        self.__board = board
        self.__ai = ai

    def __print_board(self):
        """
        Prints the game board
        :return: None
        """
        print(self.__board.show.replace('1', '\033[1m\033[94m0\033[0m').replace('2', '\033[1m\033[91m0\033[0m') + '\n')

    def menu(self):
        self.__print_board()
        while True:
            x = input("Position>")
            try:
                x = int(x)
            except ValueError:
                raise MenuException("Invalid position")
            if x not in range(1, 8):
                raise MenuException("Invalid position")
            x -= 1  # translates position as in 1 -> 0
            self.__board.add_piece(x, 1)
            self.__print_board()
            if self.__game_state(1):
                break
            self.__board.add_piece(self.__ai.generator(), 2)
            self.__print_board()
            if self.__game_state(2):
                break

    def __game_state(self, player):
        if self.__board.game_state() == 0:
            print("Draw")
            return True
        elif self.__board.game_state() == 1:
            print("Player %d won" % player)
            return True
