from player import Player,RandomPlayer,Sinnawr
from game import Game
import chess

class Tournament:

    def __init__(self, white:Player = RandomPlayer(), black:Player =  Sinnawr()):
        self.white = white
        self.black = black
        self.result={
            'White': 0,
            'Black':0
        }
    
    def start(self,numberOfGames=3):
        for i in range(numberOfGames):
            if i % 2 == 0:
                game = Game(self.white,self.black)
            else:
                game = Game(self.black,self.white)
            match = game.play()
            self.recordResult(match)
            print(match)
        self.printResult()
    
    def recordResult(self,pgn:chess.pgn.Game):
        if pgn.headers["Result"] == '1-0':
            if pgn.headers["White"] == self.white.get_name():
                self.result["White"] += 1
            else:
                self.result["Black"] += 1
        elif pgn.headers["Result"] == '0-1':
            if pgn.headers["Black"] == self.black.get_name():
                self.result["Black"] += 1
            else:
                self.result["White"] += 1
        else:
            self.result["White"] += 0.5
            self.result["Black"] += 0.5
    
    def printResult(self):
        print('{}:{} , {}:{}'.format(self.white.get_name(),self.result["White"],self.black.get_name(),self.result["Black"]))