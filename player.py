import random
import chess
from chessNode import ChessNode
import evaluation

class Player:
    def get_next_move(self,board:chess.Board):
        """ given a board the player should return a move """
        pass
    
    def get_name(self):
        pass


class RandomPlayer(Player):
    def get_next_move(self,board:chess.Board):
        return random.choice([m for m in board.legal_moves])
    
    def get_name(self):
        return 'RandomPlayer'


class Sinnawr(Player):
    def get_next_move(self,board):
        max = self.negaMax(ChessNode(board,None),3)
        return max.move
    
    def get_name(self):
        return 'Sinnawr'

    def negaMax(self,node:ChessNode,depth):
        if depth == 0:
            return ChessNode(None,None,evaluation.evaluation(node.board)) 
        max = ChessNode(None,None)
        for move in [m for m in node.board.legal_moves]:
            newNode = ChessNode(node.board,move)
            newNode.score = -1 * self.negaMax(newNode,depth-1).score
            node.children.append(newNode)
            if newNode.score >  max.score :
                max = newNode
        return max