from math import inf
import random
import numpy as np
import copy
import game
import bot
import time

class Minimax:

    

    def __init__(self) -> None:
        self.board = np.array([[0, 0, 3, 3, 3, 0, 0], [0, 0, 0, 3, 0, 0, 0], [3, 0, 2, 2, 2, 0, 3], [3, 3, 2, 1, 2, 3, 3], [3, 0, 2, 2, 2, 0, 3], [0, 0, 0, 3, 0, 0, 0], [0, 0, 3, 3, 3, 0, 0]])
        self.banned_moves = list()

    def bestMove(self, depth = 5, colour=1):
        best = list()
        best_eval = float("-inf")
        for move in self.possible_moves(colour):
            #print("eval")
            #print(move)
            #print("current board 1")
            #print(self.board)
            current_board = copy.deepcopy(self.board)
            self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
            self.update_board()
            eval = self.minimax_aB(float("-inf"), float("inf"), False, depth-1, colour) #(self, player=True, depth=5
            if eval >= best_eval and move not in self.banned_moves:
                if eval > best_eval:
                    print("hi")
                    best = list()
                    best.append(move)
                    best_eval = eval
                else:
                    best_eval = eval
                    best.append(move)
            self.board = copy.deepcopy(current_board)
            #print("current board 2")
            #print(self.board)
            #print("ok")
        #print("best")
        #print(best)
        self.banned_moves.append(move)
        return random.choice(best)
    
    def possible_moves(self, colour=1):
        moves = []
        for i in range (0, 7):
            for j in range(0, 7):
                if colour == 1:
                    if self.getPawn(i, j) == 1: #roi
                        if self.getPawn(i-1, j) == 0:
                            moves.append(((i, j), (i-1, j)))
                        if i < 6 and self.getPawn(i+1, j) == 0:
                            moves.append(((i, j), (i+1, j)))
                        if self.getPawn(i, j-1) == 0:
                            moves.append(((i, j), (i, j-1)))
                        if j < 6 and self.getPawn(i, j+1) == 0:
                            moves.append(((i, j), (i, j+1)))
                    elif self.getPawn(i, j) == 2: #blanc
                        if i > 0 and self.getPawn(i-1, j) == 0:
                            moves.append(((i,j), (i-1,j)))
                        if i < 6 and self.getPawn(i+1, j) == 0:
                            moves.append(((i,j), (i+1,j)))
                        if j > 0 and self.getPawn(i, j-1) == 0:
                            moves.append(((i,j), (i,j-1)))
                        if j < 6 and self.getPawn(i, j+1) == 0:
                            moves.append(((i,j), (i,j+1)))

                        if i > 0 and self.getPawn(i-1, j) == 0:
                            moves.append(((i,j), (i-1,j)))
                        if i < 6 and self.getPawn(i+1, j) == 0:
                            moves.append(((i,j), (i+1,j)))
                        if j > 0 and self.getPawn(i, j-1) == 0:
                            moves.append(((i,j), (i,j-1)))
                        if j < 6 and self.getPawn(i, j+1) == 0:
                            moves.append(((i,j), (i,j+1)))
                else:
                    if self.getPawn(i, j) == 3: #noir
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
        return moves
    
    def update_board(self):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.getPawn(i, j) == 2:
                    if self.getPawn(i+1, j) == 3 and self.getPawn(i+2, j) == 2:
                        self.set_pawn(i+1, j)
                    if self.getPawn(i, j+1) == 3 and self.getPawn(i, j+2) == 2:
                        self.set_pawn(i, j+1)
                if self.getPawn(i, j) == 3:
                    if self.getPawn(i+1, j) == 2 and self.getPawn(i+2, j) == 3:
                        self.set_pawn(i+1, j)
                    if self.getPawn(i, j+1) == 2 and self.getPawn(i, j+2) == 3:
                        self.set_pawn(i, j+1)

    def king_dist(self, board):
        k = self.get_pos()
        #y, x, y, x
        dist1 = abs(k[1] - 0) + abs(k[0] - 0)
        col1min = min(dist1, abs(k[1] - 0) + abs(k[0] - 6))
        linemin = min(col1min, abs(k[1] - 6) + abs(k[0] - 0))
        finalmin = min(linemin, abs(k[1] - 6) + abs(k[0] - 6))
        return finalmin
    
    def get_pos(self):
        return np.where(self.board == 1)
     
    #set current player colour in a condition to better consider captures
    def eval(self, board, isPlayer):
        #print("eval algo")
        if(self.getPawn(0, 0) == 1 or self.getPawn(6, 6) == 1 or self.getPawn(0, 6) == 1 or self.getPawn(6, 0) == 1):
            if isPlayer:
                return float("inf")
            else:
                return float("-inf")
        return self.getCount(2) - self.getCount(3) + self.king_dist(board)

    def minimax_aB(self, a, b, player=True,depth=25, colour=1):
        #successeur is knot of tree
        #successeur is populated by game class based on board state
        #state is the top node of the tree 
        #print("current depth = ", depth)
        if depth == 0:
            res = self.eval(self, player)
            return res
        if(player == True):
            max_eval = float("-inf")
            for move in self.possible_moves(colour):
                #print("current board in minimax 1")
                #print(self.board)
                current_board = copy.deepcopy(self.board)
                self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
                self.update_board()
                #print("current board in minimax 2")
                self.board = copy.deepcopy(current_board)
                #print(self.board)
                max_eval = max(self.minimax_aB(a, b, False, depth-1, colour), max_eval)
                a = max(b, max_eval)
                if b <= a:
                    return max_eval
            return max_eval
        else:
            min_eval = float("inf")
            for move in self.possible_moves(colour):
                #print("current board in minimax 3")
                #print(self.board)
                current_board = copy.deepcopy(self.board)
                self.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
                #print("current board in minimax 4")
                self.board = copy.deepcopy(current_board)
                #print(self.board)
                min_eval = max(self.minimax_aB(a, b, False, depth-1, colour), min_eval)
                b = min(b, min_eval)
                if b <= a:
                    return min_eval
            return min_eval

    #no eval for black pawns yet


    def eval_aB(self, state, a, b, score): 
        print("eval aB algo")

    def move_pawn(self, oldx, oldy, newx, newy):
        pawn = self.board[oldx,oldy]
        self.board[newx, newy]= pawn
        self.board[oldx, oldy] = 0

    def set_pawn(self, x, y):
        self.board[x, y]= 0
    
    def getPawn(self, coordx, coordy):
        return self.board[coordx, coordy]
    
    def getCount(self, occurance):
        return np.count_nonzero(self.board == occurance)
    

def main():
    minimax = Minimax()
    print("initial board")
    print(minimax.board)
    turn = True
    colour = 1 #get colour from input
    while True:
        if turn == True:
            print("turn")
            move = Minimax.bestMove(minimax, 3, colour)
            print("move")
            print(move)
            minimax.move_pawn(move[0][0], move[0][1], move[1][0], move[1][1])
            minimax.update_board()
            print(minimax.board)
            print("end turn")
            turn = False
        else:
            moves = input("enter next move: ")
            moves = moves.split(", ")
            print(moves[0], moves[1])
            minimax.move_pawn(int(moves[0]), int(moves[1]), int(moves[2]), int(moves[3]))
            minimax.update_board()
            print(minimax.board)
            time.sleep(10)
            print("end turn")
            turn = True


if __name__ == "__main__":
    main()
        


#inf values in python: https://docs.python.org/3/library/math.html#math.inf