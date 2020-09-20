from player import Player
from chessNode import ChessNode
import evaluation
import chess
import time
import random

class Sinnawr(Player):
	def __init__(self):
		self.depth= 4
		self.timeout = 30
		self.fh =0
		self.fhf=0

	def get_next_move(self,board:chess.Board):
		try:
			return chess.polyglot.MemoryMappedReader("ProDeo.bin").weighted_choice(board).move
		except:
			print('Calc:')
			move = self.get_next_move_alpha(board)
			"""
			start = time.clock()
			for self.depth in range(1,99):
				if (time.clock() - start) <= self.timeout:
						move = self.get_next_move_alpha(board)
				else:
					break
			print(self.depth)
			"""
			return move
	

	def test(self,board:chess.Board):
		start = time.clock()
		for self.depth in range(1,99):
			if (time.clock() - start) <= self.timeout:
					print(self.get_next_move_alpha(board))
			else:
				break
		"""
		while True:
			if self.depth <= 5:
				self.iterative_deepining(board)
			else:
				break		
		"""

	def get_next_move_alpha(self,board:chess.Board):
		self.fhf = 0
		self.fh = 0
		t = time.process_time()
		bestMove = chess.Move.null()
		bestValue = -evaluation.inf
		alpha =  -evaluation.inf
		beta =  evaluation.inf

		for move in self.order(board):
			board.push(move)
			boardValue = -self.alphabeta(board,-beta, -alpha, self.depth)
			if boardValue > bestValue:
				bestMove = move
				bestValue = boardValue
			if( boardValue > alpha ):
				alpha = boardValue
			board.pop()
		#print('Ordering: {}'.format((self.fhf/self.fh)*100))
		#print('calculation took :{}'.format(time.process_time() - t))
		return bestMove
	
	def get_name(self):
		return 'Flamingos'


	def alphabeta(self,board:chess.Board, alpha, beta, depthleft ):
		bestscore = -evaluation.inf
		n = 0
		if( depthleft == 0 ):
			return self.quiesce(board, alpha, beta, 3)
		
		for move in self.order(board):
			n+=1
			board.push(move)   
			score = -self.alphabeta( board,-beta, -alpha, depthleft - 1 )
			board.pop()
			if score >= beta:
				if n ==1:
					self.fhf+=1
				self.fh+=1
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

		for move in self.order(board):
			if board.is_capture(move):
				board.push(move)
				score = -self.quiesce(board,-beta, -alpha ,depthleft -1)
				board.pop()

				if score >= beta:
					return beta
				if score > alpha:
					alpha = score  
		return alpha

	def getHash(self,board:chess.Board):
		return chess.polyglot.zobrist_hash(board)

	def order(self,board:chess.Board):
		moves = self.MVVLVA(board)
		# TODO find out if the move is promotion
		return moves

	def MVVLVA(self,board:chess.Board):
		dic={}
		for move in board.legal_moves:
			if board.is_capture(move):
				# get victim type
				v = board.piece_at(move.to_square)
				# en passant 
				if v == None:
					v = chess.Piece(chess.PAWN,True)
				v = v.piece_type
				# get attacker type
				a = board.piece_at(move.from_square).piece_type
				# 105 =< value <= 605
				dic[move] = (v * 100) + 6 - (a/100)
			else:
				dic[move] = 0
		return sorted(dic,key=dic.get,reverse=True)