import random
import chess

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


class sinnawr(Player):
    def get_next_move(self,board):
        return random.choice([m for m in board.legal_moves])
    
    def get_name(self):
        return 'Sinnawr'