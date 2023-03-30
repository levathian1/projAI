from math import inf
import game

class Minimax:
    def __init__(self) -> None:
        print("minimax class")

    def minimax_aB(self, state, score, player):
        #successeur is knot of treee
        #successeur is populated by game class based on board state
        #state is the top node of the tree 
        print("minimax algo")

    #no eval for black pawns yet
    def eval(self, board, score, isPlayer):
        print("eval algo")
        if(board.getPawn[0, 0] == "k" or board.getPawn[6, 6] == "k" or board.getPawn[0, 6] == "k" or board.getPawn[6, 0] == "k"):
            if isPlayer:
                return 100
            else:
                return -100
        return board.getCount("w") - board.getCount("b")

    def eval_aB(self, state, a, b, score): 
        print("eval aB algo")


#inf values in python: https://docs.python.org/3/library/math.html#math.inf