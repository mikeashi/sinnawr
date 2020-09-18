import random
import chess
from chessNode import ChessNode
import evaluation
import chess.engine

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

class Stockfish(Player):
    def __init__(self):
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
    
    def get_next_move(self,board:chess.Board):
        return self.engine.play(board, chess.engine.Limit(time=3)).move
    
    def get_name(self):
        return 'Stockfish'


class Sinnawr(Player):

    def get_next_move(self,board:chess.Board):
        bestMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in board.legal_moves:
            board.push(move)
            boardValue = -self.alphabeta(board,-beta, -alpha, 3)
            if boardValue > bestValue:
                bestValue = boardValue;
                bestMove = move
            if( boardValue > alpha ):
                alpha = boardValue
            board.pop()
        return bestMove

    def get_name(self):
        return 'Sinnawr'

    def alphabeta(self,board:chess.Board, alpha, beta, depthleft ):
        bestscore = float('-inf')
        if( depthleft == 0 ):
            #return evaluation.evaluation(board)
            return self.quiesce(board, alpha, beta, 3)
            
        for move in board.legal_moves:
            board.push(move)   
            score = -self.alphabeta( board,-beta, -alpha, depthleft - 1 )
            board.pop()
            if score >= beta:
                return score
            if score > bestscore:
                self.bestMove = move
                bestscore = score
            if score > alpha:
                alpha = score     
        return bestscore
    
    def quiesce(self,board:chess.Board, alpha, beta, depthleft):
        stand_pat = evaluation.evaluation(board)
        if depthleft == 0 :
            return stand_pat
        if( stand_pat >= beta ):
            return beta
        if( alpha < stand_pat ):
            alpha = stand_pat

        for move in board.legal_moves:
            if board.is_capture(move):
                board.push(move)
                score = -self.quiesce(board,-beta, -alpha ,depthleft -1)
                board.pop()

                if score >= beta:
                    return beta
                if score > alpha:
                    alpha = score  
        return alpha
    

