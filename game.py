import chess
import chess.pgn
import player


class Game:
    def __init__(self, white:player , black:player):
        self.board = chess.Board()
        self.white = white
        self.black = black
        self.history = []
    
    def play(self):
        game = chess.pgn.Game()
        game.headers["White"] = self.white.get_name()
        game.headers["Black"] = self.black.get_name()
        node = game

        while not self.board.is_game_over():
            if self.board.turn:
                move = self.white.get_next_move(self.board)
            else:
                move = self.black.get_next_move(self.board)
            self.board.push(move)
            self.history.append(move)
            print(game)    
            node = node.add_variation(move)

        game.headers["Result"] = self.board.result()
        return game

    def restart(self):
        self.board = chess.Board()