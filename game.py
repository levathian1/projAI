import numpy as np

#character signification
#2: white pawns
#3: black pawns
#1: king

class Game:
    def __init__(self) -> None:
        self.board = np.matrix("0, 0, 3, 3, 3, 0, 0; 0, 0, 0, 3, 0, 0, 0; 3, 0, 2, 2, 2, 0, 3; 3, 3, 2, 1, 2, 3, 3; 3, 0, 2, 2, 2, 0, 3; 0, 0, 0, 3, 0, 0, 0; 0, 0, 3, 3, 3, 0, 0")

    #x is y and y is x in matrix arrangement
    def move_pawn(self, oldx, oldy, newx, newy):
        print(self.board)
        pawn = self.board[oldx,oldy]
        self.board[newx, newy]= pawn
        self.board[oldx, oldy] = 0
        print(self.board)