import chess
from copy import deepcopy
import chess.polyglot

class ChessNode:
    def __init__(self,board:chess.Board=None,move:chess.Move=None,score=float('-inf')):
        self.board = deepcopy(board)
        self.move  = move
        self.score = score
        if self.board != None and self.move != None:
            self.board.push(move)
        self.children=[]

    def getHash(self):
        return chess.polyglot.zobrist_hash(self.board)

    def __str__(self, level=0):
        ret = "\t"*level+repr([self.score,self.move])+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def __repr__(self):
        return '<tree node representation>'