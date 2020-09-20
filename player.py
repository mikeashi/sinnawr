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
        self.engine.configure({'Skill Level': 5})
    
    def get_next_move(self,board:chess.Board):
        move =  self.engine.play(board, chess.engine.Limit(time=3)).move
        if move in board.legal_moves :
            return move  
        return random.choice([m for m in board.legal_moves])
    
    def get_name(self):
        return 'Stockfish'
        