import numpy as np

#character signification
#2: white pawns
#3: black pawns
#1: king

class Game:
    def __init__(self) -> None:
        self.board = self.board_init()

    def board_init(self):
        self.board = np.matrix("0, 0, 3, 3, 3, 0, 0; 0, 0, 0, 3, 0, 0, 0; 3, 0, 2, 2, 2, 0, 3; 3, 3, 2, 1, 2, 3, 3; 3, 0, 2, 2, 2, 0, 3; 0, 0, 0, 3, 0, 0, 0; 0, 0, 3, 3, 3, 0, 0")
        print(self.board)
