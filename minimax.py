from math import inf
import game
import bot

class Minimax:
    def __init__(self) -> None:
        print("minimax class")

    def bestMove(self, board, player):
        best = -1000
        move = (-1, -1)
        moveVal = 0
        for i in range (0, 7):
            for j in range (0, 6):
                board = board.move_pawn(i, j, i, j+1)
                moveVal = self.eval(board, best, player)
                board = board.move_pawn(i, j, i, j-1)
                if(moveVal > best):
                    move = (i, j)
                    best = moveVal
        print("best move is: ", move[0], " ", move[1])
        print("Value of ", best)
        return (best, move)

    def minimax_aB(self, board, score, player):
        #successeur is knot of tree
        #successeur is populated by game class based on board state
        #state is the top node of the tree 
        print("minimax algo")
        best = score
        newbest = 0
        move = (-1, -1)
        if(score > 100 or score < 100):
            return score
        if(player):
            newbest = self.bestMove(board, True)
            if(best < newbest[0]):
                best = newbest[0]
                move = newbest[1]
        else:
            newbest = self.bestMove(board, False)
            if(best > newbest[0]):
                best = newbest[0]
                move = newbest[1]
        return (newbest, move)

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