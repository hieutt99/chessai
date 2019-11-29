from Board.board import Board
import copy
import settings


import time

class Tree():
	def __init__(self,board,depth,move):
		self.board = copy.deepcopy(board)
		self.children = []
		self.eval = 0
		self.depth = depth
		self.start = move[0]
		self.end = move[1]
	def point(self):
		evaluate(self.board)
		self.eval = self.board.evaluation
	def add(self,node):
		assert isinstance(node,Tree)
		self.children.append(node)

def checkEndGame(board):
	if  board.turn == 1 and settings.whiteKingCheck(board) == True : 
		if settings.checkMate(board) == True :
			board.end_game = True
	elif board.turn == -1 and settings.blackKingCheck(board) == True :
		if settings.checkMate(board) == True:
			board.end_game = True
	if 	board.number > 100 and settings.checkStalemate(board) == True :
		board.end_game = True
	# return board.end_game
def minimax(position,depth,maximizing):
	temp = position.eval
	# print(type(temp))
	if 	depth == 0 or position.board.end_game == True : 
		# print("gia tri cua minimax : "+str(eval))
		return temp
	if 	maximizing == True:
		maxEval = -10000
		for child in position.children:
			temp = minimax(child,depth-1,False)
			maxEval = max(maxEval,temp)
			position.eval = maxEval
		return position.eval
	elif maximizing == False:
		minEval = 10000
		for child in position.children:
			temp = minimax(child,depth-1,True)
			minEval = min(minEval,temp)
			position.eval = minEval
		return position.eval
def negamax(position, depth, maximizing):
	temp = position.eval
	if 	depth == 0 or position.board.end_game == True:
		return abs(temp)*maximizing
	value = -10000
	for child in position.children:
		value = max(value, -negamax(child, depth-1, - maximizing))
		position.eval = value
	return value
def abminimax(position,depth,alpha,beta,maximizing):
	temp = position.eval
	if depth == 0 or position.board.end_game == True: 
		# print("gia tri cua minimax : "+str(eval))
		return temp
	if maximizing == True:
		maxEval = -10000
		for child in position.children:
			temp = abminimax(child,depth-1,alpha,beta,False)
			maxEval = max(maxEval,temp)
			alpha = max(alpha,temp)
			position.eval = maxEval
			if beta <= alpha : 
				break
			
		return maxEval
	else :
		minEval = 10000
		for child in position.children:
			temp = abminimax(child,depth-1,alpha,beta,True)
			minEval = min(minEval,temp)
			beta = min(beta,temp)
			position.eval = minEval
			if beta <= alpha :
				break
			
		return minEval
#res = abminimax(t,depth,-10000,10000,True)
#eval maximize for black turn
def evaluate(board):
	board.evaluation = 0
	board.updatePieceForCheck()
	mobility = 0
	extra_point = 0
	for piece in board.pieces:
		temp = piece[0].availableMoves(board)
		mobility -= len(temp)*piece[0].alliance
	settings.kingPosition(board)
	if 	board.whiteKing[0].moved == True and board.whiteKing[0].castle == True : 
		extra_point += 20*(-1)
	elif board.whiteKing[0].moved == True and board.whiteKing[0].castle == False : 
		extra_point -= 20*(-1)
	if 	board.blackKing[0].moved == True and board.blackKing[0].castle == True :
		extra_point	+= 20*1
	elif board.blackKing[0].moved == True and board.blackKing[0].castle == False : 
		extra_point -= 20*1 

	checkEndGame(board)
	if 	board.end_game == False:
		for piece in board.pieces :
			board.evaluation -= piece[0].point
	else :
		if  settings.whiteKingCheck(board) == True : 
			if settings.checkMate(board) == True :
				board.evaluation += 9000
		elif settings.blackKingCheck(board) == True :
			if settings.checkMate(board) == True:
				board.evaluation += -9000
		if 	board.number > 100 and settings.checkStalemate(board) == True :
			board.evaluation = 0
	board.evaluation += mobility+extra_point
	# print("Evaluation : " + str(board.evaluation))
def translateMoveBot(board,move):
	default = board.default
	for key, val in default.items():	
		if move[0] == val :
			start = key
		if move[1] == val :
			end = key
	return start, end
def printTree_pre(tree):
	if tree == None : 
		print("Tree is empty")
		return
	else :
		# tree.board.printBoard()
		print(tree.eval, end = ' ')		
		print(tree.depth)

		for i in range(len(tree.children)):
			printTree_pre(tree.children[i])
def botMove_temp(board):
	print("Generating moves...")
	# turn = -1
	x = copy.deepcopy(board)
	depth = 2
	t = Tree(board = x, depth = depth,move = move)
	stack = []
	stack.append(t)
	top = 0

	while top != -1 and depth >= 0	:
		temp = stack.pop(top)
		top = top-1

		depth = temp.depth
		print("temp.depth:") 
		print(temp.depth)

		# temp.board.legalMoves = []
		temp.board.updatePieceForCheck()
		checkEndGame(temp.board)
		print("turn : ")
		print(temp.board.turn)
		
		if 	temp.board.end_game != True and depth >= 0 	:
			temp.board.legalMoves = []
			depth -= 1
			print(depth)
			temp.board.movesForBot = []
			for piece in temp.board.pieces:
				if 	piece[0].alliance == temp.board.turn :
					print("check :")
					print(piece[0].alliance)
					print(piece[0].symbol())
					print(temp.board.turn)
					temp.board.legalMoves = piece[0].availableMoves(temp.board)
					settings.checkLegal(temp.board)
					for move in temp.board.legalMoves:
						temp.board.movesForBot.append([piece[0].position,move])
	
				for move in temp.board.movesForBot :
					start,end = translateMoveBot(temp.board,move)

					y = copy.deepcopy(temp.board)
					y.updateMove(start,end)

					temp.add(Tree(board = y, depth = depth,move = move))

			for child in temp.children:
				stack.append(child)
			top += len(temp.children)
		else :
			temp.point()
	
	print("Calculating moves...")


	print("pre order traversal : ")
	printTree_pre(t)


	# depth = 3 
	# move_point = minimax(t,depth,True)

	# for i in t.children:
	# 	if (i.eval == t.eval):
	# 		chosen = i.board

	print("Finished Calculating!")
	# return chosen

def botMove(board):
	print("Generating moves ...")

	time_start = time.time()
	depth = 2

	t = Tree(board = board, depth = depth, move = [[0,0],[0,0]])
	stack = []
	stack.append(t)
	top = 0

	while top != -1:
		# print(top)
		temp = stack.pop(top)
		top = top - 1

		depth = temp.depth

		temp.board.updatePieceForCheck()
		checkEndGame(temp.board)

		if temp.board.end_game != True and depth != 0:
			depth -= 1

			temp.board.legalMoves = []
			temp.board.movesForBot = []
			for piece in temp.board.pieces:
				if 	piece[0].alliance == temp.board.turn:
					temp.board.legalMoves = piece[0].availableMoves(temp.board)
					for key,val in temp.board.default.items() :
						if piece[0].position == val :
							temp.board.start = key
					settings.checkLegal(temp.board)
					for move in temp.board.legalMoves :
						temp.board.movesForBot.append([piece[0].position,move])
				# if 	piece[0].symbol() == 'k':
				# 	print(temp.board.legalMoves)

			for move in temp.board.movesForBot :
				start, end = translateMoveBot(temp.board,move)

				y = copy.deepcopy(temp.board)
				y.updateMove(start,end)

				temp.add(Tree(board = y, depth = depth, move= move))
				# print(move)

			for child in temp.children:
				stack.append(child)
			top += len(temp.children)

		else :
			temp.point()

	# temp = t.children[0]
	# temp.board.updatePieceForCheck()
	# print("children 0 :")
	# temp.board.printBoard()
	# print("************************************************")
	# temp.board.legalMoves = []
	# temp.board.movesForBot = []
	# for piece in temp.board.pieces :
	# 	# print("=====test====")
	# 	# print(piece[0].symbol())
	# 	# print(temp.board.turn)
	# 	# print("$$$$$$$$$$$$$")
	# 	if 	piece[0].alliance == temp.board.turn :
	# 		# print("=====test====")
	# 		# print(piece[0].symbol())
	# 		# print(temp.board.turn)
	# 		# print("$$$$$$$$$$$$$")
	# 		temp.board.legalMoves = piece[0].availableMoves(temp.board)
	# 		settings.checkLegal(temp.board)
	# 		for move in temp.board.legalMoves:
	# 			temp.board.movesForBot.append([piece[0].position,move])
	# for move in temp.board.movesForBot:
	# 	start, end = translateMoveBot(temp.board, move)
	# 	# print("test")
	# 	y = copy.deepcopy(temp.board)
	# 	# y.printBoard()
	# 	y.updateMove(start,end)
	# 	temp.add(Tree(board = y, depth = 1, move = move))
	# 	# print(start + end)
	# 	# y.printBoard()
	# 	# print("******************")

	# temp = t.children[0].children[0]
	# temp.board.updatePieceForCheck()
	# print("children 0 :")
	# temp.board.printBoard()
	# print("************************************************")
	# temp.board.legalMoves = []
	# temp.board.movesForBot = []
	# for piece in temp.board.pieces :
	# 	# print("=====test====")
	# 	# print(piece[0].symbol())
	# 	# print(temp.board.turn)
	# 	# print("$$$$$$$$$$$$$")
	# 	if 	piece[0].alliance == temp.board.turn :
	# 		print("=====test====")
	# 		print(piece[0].symbol())
	# 		print(temp.board.turn)
	# 		print("$$$$$$$$$$$$$")
	# 		temp.board.legalMoves = piece[0].availableMoves(temp.board)
	# 		settings.checkLegal(temp.board)
	# 		for move in temp.board.legalMoves:
	# 			temp.board.movesForBot.append([piece[0].position,move])
	# for move in temp.board.movesForBot:
	# 	start, end = translateMoveBot(temp.board, move)
	# 	print("test")
	# 	y = copy.deepcopy(temp.board)
	# 	y.printBoard()
	# 	y.updateMove(start,end)
	# 	print(start + end)
	# 	y.printBoard()
	# 	print("******************")

	# 	temp.add(Tree(board = y, depth = depth, move  =move))
	# print("Calculating moves...")

	# for case in t.children[0].children:
	# 	case.board.printBoard()

	# print("pre order traversal : ")
	# printTree_pre(t)
	# print("\n==================")
	time_end = time.time()

	seconds = time_end-time_start
	print("Create tree, time : "+str(seconds)+"    ... time lapse...")
	depth = 2
	# move_point = minimax(t,depth,True)
	move_point = abminimax(t,depth,-10000,10000,True)

	# print("pre order traversal : ")
	# printTree_pre(t)
	# print("\n==================")


	# evaluate(t.board)
	# print("test : " + str(t.board.evaluation))


	# print(" test evaluation : ")
	# for i in t.children:
	# 	print(i.eval,end = ' ')
	# print("test evaluation 2 : ")
	# for i in t.children :
	# 	for j in i.children : 
	# 		print(j.eval,end = ' ')
	for i in t.children:
		if (i.eval == t.eval):
			start,end = translateMoveBot(i.board,[i.start,i.end])
			break
	print(move_point)

	# print("test : ")
	# filename = open("data.board",'w')
	# pickle.dump(t,filename)
	time_end = time.time()
	seconds = time_end - time_start 
	print("time total : "+str(seconds))

	print("Finished Calculating!")
	return start, end


def createTree(board):
	print("Generating moves ...")

	time_start = time.time()
	depth = 2

	t = Tree(board = board, depth = depth, move = [[0,0],[0,0]])
	stack = []
	stack.append(t)
	top = 0

	while top != -1:
		temp = stack.pop(top)
		top = top - 1

		depth = temp.depth

		temp.board.updatePieceForCheck()
		checkEndGame(temp.board)

		if temp.board.end_game != True and depth != 0:
			depth -= 1

			temp.board.legalMoves = []
			temp.board.movesForBot = []
			for piece in temp.board.pieces:
				if 	piece[0].alliance == temp.board.turn:
					temp.board.legalMoves = piece[0].availableMoves(temp.board)
					for key,val in temp.board.default.items() :
						if piece[0].position == val :
							temp.board.start = key
					settings.checkLegal(temp.board)
					for move in temp.board.legalMoves :
						temp.board.movesForBot.append([piece[0].position,move])

			for move in temp.board.movesForBot :
				start, end = translateMoveBot(temp.board,move)

				y = copy.deepcopy(temp.board)
				y.updateMove(start,end)

				temp.add(Tree(board = y, depth = depth, move= move))
				# print(move)

			for child in temp.children:
				stack.append(child)
			top += len(temp.children)

		else :
			temp.point()
	time_end = time.time()
	print("time to create Tree : " + str(time_end-time_start))
	return t
def updateTree(board,tree):
	for i in tree.children :
		if board.start == i.start and board.end == i.end :
			break
def moveOfBot(board,tree):
	print("Start Calculating...")
	# print("first, traversal : ")
	# printTree_pre(tree)
	time_start = time.time()
	depth = 2
	# move_point = minimax(tree,depth,True)
	# move_point = abminimax(tree,depth,-10000,10000,True)
	move_point = negamax(tree,depth, -1)


	#for minimax and alpha beta 
	# for i in tree.children:
	# 	if (i.eval == tree.eval):
	# 		start,end = translateMoveBot(i.board,[i.start,i.end])
	# 		break

	#for negamax only
	start=""
	end = ""
	for i in tree.children:
		# print(i.eval,end = ' ')
		if (i.eval == -tree.eval):
			start,end = translateMoveBot(i.board,[i.start,i.end])
			break

	if (start == "" or end ==""):
		print("Error processing move!!!")
		return None,None

	print("point of the chosen move : "+str(move_point) )

	time_end = time.time()
	seconds = time_end - time_start 
	print("Time taken to implement algo : "+str(seconds))

	print("Finished Calculating!")
	return start, end