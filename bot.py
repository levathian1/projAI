import minimax
import game

class Bot:
    def __init__(self) -> None:
        pass

    #send to minimax
    def bestMove(board, player):
        best = -1000
        move = (-1, -1)
        moveVal = 0
        for i in range (0, 7):
            for j in range (0, 6):
                board = board.move_pawn(i, j, i, j+1)
                moveVal = minimax(board, player)
                board = board.move_pawn(i, j, i, j-1)
                if(moveVal > best):
                    move = (i, j)
                    best = moveVal
        print("best move is: ", move[0], " ", move[1])
        print("Value of ", best)
        return best
