import chess

inf = 30000
mate = 29000

wights = {chess.KING: 20000,chess.QUEEN: 900,chess.ROOK: 500,chess.KNIGHT:320,chess.BISHOP:330,chess.PAWN:100}

mpst = {
	chess.PAWN :[
					 0,  0,  0,  0,  0,  0,  0,  0,
					-7,  7, -3,-13,  5,-16, 10, -8,
					 5,-12, -7, 22, -8, -5,-15, -8,
					13,  0,-13,  1, 11, -2,-13,  5,
					-4,-23,  6, 20, 40, 17,  4, -8,
					-9,-15, 11, 15, 32, 22,  5,-22,
					 3,  3, 10, 19, 16, 19,  7, -5,
					 0,  0,  0,  0,  0,  0,  0,  0
				],
	chess.BISHOP :[
					-48,  1,-14,-23,-23,-14, 1,-48,
					-17,-14,  5,  0,  0,  5,-14,-17,
					-16,  6,  1, 11, 11,  1,  6,-16,
					-12, 29, 22, 31, 31, 22, 29,-12,
					 -5, 11, 25, 39, 39, 25, 11, -5,
					 -7, 21, -5, 17, 17, -5, 21, -7,
					-15,  8, 19,  4,  4, 19,  8,-15,
					-53, -5, -8,-23,-23, -8, -5,-53
				 ],
	chess.KNIGHT :[
					-201,-83,-56,-26,-26,-56,-83,-201,
					-67,-27,  4, 37, 37,  4,-27,-67,
					- 9, 22, 58, 53, 53, 58, 22,- 9,
					-34, 13, 44, 51, 51, 44, 13,-34,
					-35,  8, 40, 49, 49, 40,  8,-35,
					-61,-17,  6, 12, 12,  6,-17,-61,
					-77,-41,-27,-15,-15,-27,-41,-77,
					-175,-92,-74,-73,-73,-74,-92,-175
				 ],
	chess.ROOK : [
					-17,-19,- 1,  9,  9,- 1,-19,-17,
					- 2, 12, 16, 18, 18, 16, 12,- 2,
					-22,- 2,  6, 12, 12,  6,- 2,-22,
					-27,-15,- 4,  3,  3,- 4,-15,-27,
					-13,- 5,- 4,- 6,- 6,- 4,- 5,-13,
					-25,-11,- 1,  3,  3,- 1,-11,-25,
					-21,-13,- 8,  6,  6,- 8,-13,-21,
					-31,-20,-14,- 5,- 5,-14,-20,-31,
				 ],
	chess.QUEEN : [
					- 2,- 2,  1,- 2,- 2,  1,- 2,- 2,
					- 5,  6, 10,  8,  8, 10, 6,- 5,
					- 4, 10,  6,  8,  8,  6, 10,- 4,
					  0, 14, 12,  5,  5, 12, 14,  0,
					  4,  5,  9,  8,  8,  9,  5,  4,
					- 3,  6, 13,  7,  7, 13,  6,- 3,
					- 3,  5,  8, 12, 12,  8,  5,- 3,
					  3,- 5,- 5,  4,  4,- 5,- 5,  3,
				 ],
	chess.KING : [
					 59, 89, 45, -1, -1, 45, 89, 59,
					 88,120, 65, 33, 33, 65,120, 88,
					123,145, 81, 31, 31, 81,145,123,
					154,179,105, 70, 70,105,179,154,
					164,190,138, 98, 98,138,190,164,
					195,258,169,120,120,169,258,195,
					278,303,234,179,179,234,303,278,
					271,327,271,198,198,271,327,271,
				 ]		 
}

epst = {
	chess.PAWN :[
					 0,  0,  0,  0,  0,  0,  0,  0,
					 0,  -11, 12,21,  25,19, 4, 7,
					 28,20, 21, 28, 30, 7,6, 13,
					10,  5,4,  -5, -5, -5,14,  9,
					6,-2,  -8, -4, -13, -12,  -10, -9,
					-10,-10, -10, 4, 4, 3,  -6,-4,
					 -10,  -6, 10, 0, 14, 7,  -5, -19,
					 0,  0,  0,  0,  0,  0,  0,  0
				],
	chess.BISHOP :[
					-46,  -42,-37,-24,-24,-37, -42,-46,
					-31,-20,  -1,  1,  1,  -1,-20,-31,
					-30,  6,  4, 6, 6,  4,  6, -30,
					-17, -1,-14, 15, 15, -14, -1,-17,
					-20, -6, 0, 17, 17, 0, -6, -20,
					-16, -1, -2, 10, 10,  -2, -1, -16,					 
					-37,  -13, -17,  1,  1, -17,  -13,-37,
					-57, -30, -37,-12,-12, -37, -30,-57
				 ],
	chess.KNIGHT :[
					-201,-83,-56,-26,-26,-56,-83,-201,
					-67,-27,  4, 37, 37,  4,-27,-67,
					- 9, 22, 58, 53, 53, 58, 22,- 9,
					-34, 13, 44, 51, 51, 44, 13,-34,
					-35,  8, 40, 49, 49, 40,  8,-35,
					-61,-17,  6, 12, 12,  6,-17,-61,
					-77,-41,-27,-15,-15,-27,-41,-77,
					-175,-92,-74,-73,-73,-74,-92,-175
				 ],
	chess.ROOK : [
					18,0,19,  13,  13,19,0,18,
					4, 5, 20, -5, -5, 20, 5,4,
					6,1,  -7, 10, 10,  -7,1,6,
					-5,8,7,  -6,  -6,7,8,-5,
					-6,1,-9,7,7,-9,1,-6,			 
					6,-8,-2,  -6,  -6,-2,-8,6,
					-12,-9,-1,  -2,  -2,-1,-9,-12,
					-9,-13,-10,-9,-9,-10,-13,-9,
				 ],
	chess.QUEEN : [
					-75,-52,  -43,-36,-36,  -43,-52,-75,
					-50,  -27, -24,  -8,  -8, -24, -27,-50,			
					-38, -18,  -12,  1,  1,  -12, -18,-38,
					-29, -6, 9,  21,  21, 9, -6,  -29,
					-23,  -3,  13,  24,  24,  13,  -3,  -23,
					-39,  -18, -9,  3,  3, -9,  -18,-39,
					-55,  -31,  -22, -4, -4,  -22,  -31,-55,
					 -69,-57,-47,  -26,  -26,-47,-57,  -69,
				 ],
	chess.KING : [
					 11, 59, 73, 78, 78, 73, 59, 11,
					 47,121, 116, 131, 131, 116,121, 47,
					92,172, 184, 191, 191, 184,172,92,
					96,166,199, 199, 199,199,166,96,
					103,156,172, 172, 172,172,156,103,
					88,130,169,175,175,169,130,88,
					53,100,133,135,135,133,100,53,
					1,45,85,76,76,85,45,1,
				 ]		 
}



def pieceSquareScore(board:chess.Board):
    return whitePieceSquareScore(board) - blackPieceSquareScore(board)

def materialScore(board:chess.Board):
    """
    Returns the material score of the given board
    """
    score = 0
    for piece in wights:
        score += wights[piece] * getPieceCountDiff(board,piece)
    return score



def evaluation(board:chess.Board):
	# is board in checkmate
	if board.is_checkmate():
		if(board.turn):
			return mate
		return -mate
	# is it a draw
	if is_draw(board):
		return 0
    
	return (materialScore(board) + pieceSquareScore(board)) * eval_signal(board)


######################################################################
############################# [ HELPERS] #############################
######################################################################

def getPieceCount(board:chess.Board, piece_type: chess.PieceType, color: chess.Color):
    """
    Returns the count of the given pice type for the given color.
    """
    return len(board.pieces(piece_type,color))



def getPieceCountDiff(board:chess.Board, piece_type: chess.PieceType):
    """
    Returns the difference of the count of the given pice type between the two players.
    """
    return getPieceCount(board,piece_type,chess.WHITE) - getPieceCount(board,piece_type,chess.BLACK)


def is_draw(board):
    return board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition()


def eval_signal(board:chess.Board):
    if(board.turn):
        return 1
    return -1

def whitePieceSquareScore(board:chess.Board):
	table = piceSquareTable(board)
	score = 0
	for pieceType in table:
		score = score + sum([table[pieceType][i] for i in board.pieces(pieceType, chess.WHITE)])
	return score

def blackPieceSquareScore(board:chess.Board):
	table = piceSquareTable(board)
	score = 0
	for pieceType in mpst:
		score= score + sum([table[pieceType][chess.square_mirror(i)] for i in board.pieces(pieceType, chess.BLACK)])
	return score

def piceSquareTable(board:chess.Board):
	if isMiddleGame(board):
		return mpst
	return epst

def isMiddleGame(board:chess.Board):
	return True
	if getPieceCount(board,chess.QUEEN,chess.BLACK) + getPieceCount(board,chess.QUEEN,chess.WHITE) == 0:
		return False
	return True