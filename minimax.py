from math import inf
import numpy as np
import copy
import game
import bot
import time

class Minimax:
    def __init__(self) -> None:
        self.board = np.array([[0, 0, 3, 3, 3, 0, 0], [0, 0, 0, 3, 0, 0, 0], [3, 0, 2, 2, 2, 0, 3], [3, 3, 2, 1, 2, 3, 3], [3, 0, 2, 2, 2, 0, 3], [0, 0, 0, 3, 0, 0, 0], [0, 0, 3, 3, 3, 0, 0]])

    def bestMove(self, depth = 5):
        best = None
        best_eval = float(-inf)
        for move in self.possible_moves():
            #print("eval")
            #print(move)
            #print("current board 1")
            #print(self.board)
            current_board = copy.deepcopy(self.board)
            self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
            eval = self.minimax_aB(False, depth-1) #(self, player=True, depth=5
            if eval > best_eval:
                best = move
                best_eval = eval
            self.board = copy.deepcopy(current_board)
            #print("current board 2")
            #print(self.board)
            #print("ok")
        #print("best")
        #print(best)
        return best
    
    def possible_moves(self):
        moves = []
        for i in range (0, 7):
            for j in range(0, 7):
                if self.getPawn(i, j) == 1:
                    if self.getPawn(i-1, j) == 0:
                        moves.append(((i, j), (i-1, j)))
                    if i < 6 and self.getPawn(i+1, j) == 0:
                        moves.append(((i, j), (i+1, j)))
                    if self.getPawn(i, j-1) == 0:
                        moves.append(((i, j), (i, j-1)))
                    if j < 6 and self.getPawn(i, j+1) == 0:
                        moves.append(((i, j), (i, j+1)))
                elif self.getPawn(i, j) == 3:
                    if i > 0 and self.getPawn(i-1, j) == 0:
                        moves.append(((i,j), (i-1,j)))
                    if i < 6 and self.getPawn(i+1, j) == 0:
                        moves.append(((i,j), (i+1,j)))
                    if j > 0 and self.getPawn(i, j-1) == 0:
                        moves.append(((i,j), (i,j-1)))
                    if j < 6 and self.getPawn(i, j+1) == 0:
                        moves.append(((i,j), (i,j+1)))
                    if i > 1 and self.getPawn(i-1, j) == 1 and self.getPawn(i-2, j) == 0:
                        moves.append(((i,j), (i-2,j)))
                    if i < 5 and self.getPawn(i+1, j) == 1 and self.getPawn(i+2, j) == 0:
                        moves.append(((i,j), (i+2,j)))
                    if j > 1 and self.getPawn(i, j-1) == 1 and self.getPawn(i, j-2) == 0:
                        moves.append(((i,j), (i,j-2)))
                    if j < 5 and self.getPawn(i, j+1) == 1 and self.getPawn(i, j+1) == 0:
                        moves.append(((i,j), (i,j+2)))
                elif self.getPawn(i, j) == 2:
                    if i > 0 and self.getPawn(i-1, j) == 1:
                        moves.append(((i,j), (i-1,j)))
                    if i < 6 and self.getPawn(i+1, j) == 1:
                        moves.append(((i,j), (i+1,j)))
                    if j > 0 and self.getPawn(i, j-1) == 1:
                        moves.append(((i,j), (i,j-1)))
                    if j < 6 and self.getPawn(i, j+1) == 1:
                        moves.append(((i,j), (i,j+1)))
        return moves
    
    def eval(self, score, isPlayer):
        #print("eval algo")
        if(self.getPawn(0, 0) == 1 or self.getPawn(6, 6) == 1 or self.getPawn(0, 6) == 1 or self.getPawn(6, 0) == 1):
            if isPlayer:
                return 100
            else:
                return -100
        return self.getCount("w") - self.getCount("b")

    def minimax_aB(self, player=True, depth=5):
        #successeur is knot of tree
        #successeur is populated by game class based on board state
        #state is the top node of the tree 
        #print("current depth = ", depth)
        if depth == 0:
            res = self.eval(self, player)
            return res
        if(player == True):
            max_eval = float(-inf)
            for move in self.possible_moves():
                #print("current board in minimax 1")
                #print(self.board)
                current_board = copy.deepcopy(self.board)
                self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
                evaluate = self.minimax_aB(False, depth-1)
                #print("current board in minimax 2")
                self.board = copy.deepcopy(current_board)
                #print(self.board)
                max_eval = max(evaluate, max_eval)
            return max_eval
        else:
            min_eval = float(inf)
            for move in self.possible_moves():
                #print("current board in minimax 3")
                #print(self.board)
                current_board = copy.deepcopy(self.board)
                self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
                eval = self.minimax_aB(True, depth-1)
                #print("current board in minimax 4")
                self.board = copy.deepcopy(current_board)
                #print(self.board)
                min_eval = min(eval, min_eval)
            return min_eval

    #no eval for black pawns yet


    def eval_aB(self, state, a, b, score): 
        print("eval aB algo")

    def move_pawn(self, oldx, oldy, newx, newy):
        pawn = self.board[oldx,oldy]
        self.board[newx, newy]= pawn
        self.board[oldx, oldy] = 0
    
    def getPawn(self, coordx, coordy):
        return self.board[coordx, coordy]
    
    def getCount(self, occurance):
        return np.count_nonzero(self.board == 1)
    

def main():
    minimax = Minimax()
    print("initial board")
    print(minimax.board)
    turn = False
    while True:
        if turn == False:
            print("turn")
            move = Minimax.bestMove(minimax, 3)
            print("move")
            print(move)
            minimax.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
            print(minimax.board)
            print("end turn")
            turn = True
        else:
            moves = input("enter next move: ")
            moves = moves.split(", ")
            print(moves[0], moves[1])
            minimax.move_pawn(int(moves[0]), int(moves[1]), int(moves[2]), int(moves[3]))
            print(minimax.board)
            time.sleep(10)
            print("end turn")
            turn = False


if __name__ == "__main__":
    main()
        


#inf values in python: https://docs.python.org/3/library/math.html#math.inf