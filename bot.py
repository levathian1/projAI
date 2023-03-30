import minimax
import game

class Bot:
    def __init__(self) -> None:
        pass

    #send to minimax
    def bestMove(board):
        best = -1000
        for i in range (0, 7):
            for j in range (0, 6):
                board = board.move_pawn(i, j, i, j+1)
                best = max(best, minimax(board, best, False))
        return best
