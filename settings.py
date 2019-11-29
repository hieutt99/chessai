import pygame   
import sys
import copy
from Board.board import Board
from Board.tile import Tile
from Pieces.NullPiece import NullPiece
from image import Image

import bot

def check_events(screen,board):
    mx = 0
    my = 0
    for event in pygame.event.get():
        if  event.type == pygame.QUIT :
            board.end_game = True
        # or event.key == pygame.K_ESCAPE :
            sys.exit()
        if  event.type == pygame.MOUSEBUTTONDOWN and board.selectedStartTile.tileCoordinate == []:
            board.mx,board.my = pygame.mouse.get_pos()
            for i in range(8):
                for j in range(8):
                    if board.gameTiles[i][j].pos[0]<board.mx<board.gameTiles[i][j].pos[0]+60:
                        if board.gameTiles[i][j].pos[1]<board.my<board.gameTiles[i][j].pos[1]+60:
                            board.selectedStartTile = board.gameTiles[i][j]
            if  board.selectedStartTile.pieceOnTile.symbol() != " " and\
                board.selectedStartTile.pieceOnTile.alliance == board.turn:
                board.legalMoves = board.selectedStartTile.pieceOnTile.availableMoves(board)
                # print(board.legalMoves)
                for key, value in board.default.items():
                    if  board.selectedStartTile.pieceOnTile.position == value:
                        board.start = key 
                # can ham de loai bo nuoc khong hop le
                checkLegal(board)
                #====================
                print(board.start,end = "->")
                print(board.legalMoves)
                print("available moves : ",end="")
                for key, value in board.default.items():
                    for move in board.legalMoves:
                        if(move == value):
                                print(key,end = " ")
                print("\n",end = "")
            elif (board.selectedStartTile.pieceOnTile.symbol != " " and \
                board.selectedStartTile.pieceOnTile.alliance != board.turn) or\
                board.selectedStartTile.pieceOnTile.symbol == " ":
                board.selectedStartTile = Tile([],NullPiece([]))
            else :
                board.selectedStartTile = Tile([],NullPiece([]))
            updateScreen(screen,board)
            # pygame.display.flip()
            # print("vao day")
        elif  event.type == pygame.MOUSEBUTTONDOWN and board.selectedStartTile.tileCoordinate\
            != [] :
            if len(board.legalMoves)>0:
                board.mx, board.my = pygame.mouse.get_pos()
                for i in range(8):
                    for j in range(8):
                        if board.gameTiles[i][j].pos[0]<board.mx<board.gameTiles[i][j].pos[0]+60:
                            if board.gameTiles[i][j].pos[1]<board.my<board.gameTiles[i][j].pos[1]+60:
                                board.selectedEndTile = board.gameTiles[i][j]
                                # print(board.gameTiles[i][j].pieceOnTile.symbol())
                                # print(board.selectedEndTile.tileCoordinate)
                check = 0
                for move in board.legalMoves:
                    if  move == board.selectedEndTile.tileCoordinate:
                        for key, value in board.default.items():
                            if move == value:
                                board.end = key
                                # print(board.end)
                        board.updateMove(board.start,board.end)
                        kingPosition(board)
                        updateScreen(screen,board)
                        print(board.selectedEndTile.pieceOnTile.symbol()+board.start+board.end)
                        board.selectedStartTile = Tile([],NullPiece([]))
                        board.selectedEndTile = Tile([],NullPiece([]))
                        board.legalMoves = []
                        check = 1
                        board.printBoard()
                if check == 0 :
                    board.selectedStartTile = Tile([],NullPiece([]))
                    board.selectedEndTile = Tile([],NullPiece([]))
                    board.legalMoves = []
                    updateScreen(screen,board)
            elif len(board.legalMoves) == 0 :
                board.selectedEndTile = Tile([],NullPiece([]))
                board.selectedStartTile = Tile([],NullPiece([]))
                board.legalMoves = []
                updateScreen(screen,board)
            if  whiteKingCheck(board) == True : 
                if checkMate(board) == True:
                    board.end_game = True
                else :
                    print("White King is checked ")
            elif blackKingCheck(board) == True :
                if checkMate(board) == True:
                    board.end_game = True
                else :
                    print("Black King is checked")
            if checkStalemate(board) == True :
                board.end_game = True
            bot.evaluate(board)
            print("White turn over, Board Analysis : "+str(-board.evaluation))
#=============================KING CHECK=====================================
def kingPosition(board):
    for piece in board.pieces :
        if  piece[0].symbol() == "K" :
            board.whiteKing = [piece[0],piece[0].position]
        elif piece[0].symbol() == "k":
            board.blackKing = [piece[0],piece[0].position]
            # print(board.blackKing)
def whiteKingCheck(board):
    kingPosition(board)

    for piece in board.pieces:
        if  piece[0].symbol() != "K" and piece[0].alliance != 1:
            moves = piece[0].availableMoves(board)
            # print("vao day")
            # print("test")
            # print(moves)
            # if len(moves) != 0:
            for move in moves : 
                if move == board.whiteKing[1] :
                    # print("test white king check"+piece[0].symbol()+"->"+str(move))
                    board.whiteKing[0].check = True
                    return True
    board.whiteKing[0].check = False 
    return False
def blackKingCheck(board):
    kingPosition(board)

    for piece in board.pieces:
        if  piece[0].symbol() != "k" and piece[0].alliance != -1:
            moves = piece[0].availableMoves(board)
            # print("test")
            # print(moves)
            # print(piece[0].symbol())
            # if  len(moves) != 0:
            for move in moves : 
                if move == board.blackKing[1] :
                    # print("test black king check"+piece[0].symbol()+"->"+str(move))
                    board.blackKing[0].check = True
                    return True
    board.blackKing[0].check = False
    return False
def checkLegal(board):
    temp = Board()
    # print("legal move ")
    delete = []
    if  board.turn == 1 :
        for move in board.legalMoves :
            temp = copy.deepcopy(board)
            for x,y in temp.default.items():
                if  y == move :
                    temp.updateMove(temp.start, x)
                    # temp.printBoard()
                    temp.updatePieceForCheck()
                    if whiteKingCheck(temp) == True :
                        delete.append(move)
    elif board.turn == -1 :
        for move in board.legalMoves :
            temp = copy.deepcopy(board)
            for x,y in temp.default.items():
                if  y == move :
                    temp.updateMove(temp.start, x)
                    # temp.printBoard()
                    temp.updatePieceForCheck()
                    if  blackKingCheck(temp) == True :
                        delete.append(move)
    for move in delete:
        board.legalMoves.remove(move)
    # print(board.legalMoves)
def checkMate(board):
    temp = Board()
    count = 0
    if  board.turn == 1 and whiteKingCheck(board) == True:
        for piece in board.pieces:
            if piece[0].alliance == 1:
                board.legalMoves = piece[0].availableMoves(board)
            for x, y in board.default.items():
                if y == piece[0].position:
                    board.start = x
            checkLegal(board)
            count += len(board.legalMoves)
            for move in board.legalMoves:
                temp = copy.deepcopy(board)
                for x,y in temp.default.items():
                    if y == move:
                        temp.updateMove(temp.start,x)
                        temp.updatePieceForCheck()
                        if  whiteKingCheck(temp) == True : 
                            print("Checkmate! Black wins the game")
                            return True
                        else:
                            return False 
        if  count == 0 :
            print("Checkmate! Black wins the game")
            return True
    if  board.turn == -1 and blackKingCheck(board) == True:
        for piece in board.pieces:
            if piece[0].alliance == -1:
                board.legalMoves = piece[0].availableMoves(board)
            for x, y in board.default.items():
                if y == piece[0].position:
                    board.start = x
            checkLegal(board)
            count += len(board.legalMoves)
            for move in board.legalMoves:
                temp = copy.deepcopy(board)
                for x,y in temp.default.items():
                    if y == move:
                        temp.updateMove(temp.start,x)
                        # temp.printBoard()
                        temp.updatePieceForCheck()
                        if  blackKingCheck(temp) == True : 
                            print("Checkmate! White wins the game")
                            return True
                        else:
                            return False 
        if  count == 0 :
            print("Checkmate! White wins the game")
            return True
def checkStalemate(board):
    temp = Board()
    count = 0
    if  board.turn == 1 and whiteKingCheck(board) == False:
        for piece in board.pieces:
            if piece[0].alliance == 1:
                board.legalMoves = piece[0].availableMoves(board)
            checkLegal(board)
            count += len(board.legalMoves)
            if count != 0 :
                return False
        if  count == 0 :
            print("Stalemate! White turn")
            return True
    if  board.turn == -1 and blackKingCheck(board) == False:
        for piece in board.pieces:
            if piece[0].alliance == -1:
                board.legalMoves = piece[0].availableMoves(board)
            checkLegal(board)
            count += len(board.legalMoves)
            if count != 0 :
                return False
        if  count == 0 :
            print("Stalemate! Black turn")
            return True
#=============================UPDATE SCREEN==================================
def squares(screen,x,y,w,h,color):
    pygame.draw.rect(screen, color, [x,y,w,h])

def drawChess(screen,board):
    xpos = 0
    ypos = 0
    color = 0
    width = 60
    height = 60
    # black = (60,134,244)
    black  = (64,64,64)
    # white = (143,155,175)
    white = (255,153,153)
    orange = (255,165,0)
    pieces = []
    for i in range(8):
        for j in range(8):
            board.gameTiles[i][j].pos.append(xpos)
            board.gameTiles[i][j].pos.append(ypos)
            if color % 2 == 0 :
                if  board.selectedStartTile.tileCoordinate == [i,j] or ([i,j] in board.legalMoves == True):
                    squares(screen,xpos,ypos,width,height,orange)
                else:
                    squares(screen,xpos,ypos,width,height,white)
                if board.gameTiles[i][j].pieceOnTile.symbol() != " ":
                    pieces.append([board.gameTiles[i][j].pieceOnTile,[xpos,ypos]])
                xpos += 60
            else :
                if  board.selectedStartTile.tileCoordinate == [i,j] or ([i,j] in board.legalMoves == True):
                    squares(screen,xpos,ypos,width,height,orange)
                else:
                    squares(screen,xpos,ypos,width,height,black)
                if board.gameTiles[i][j].pieceOnTile.symbol() != " ":
                    pieces.append([board.gameTiles[i][j].pieceOnTile,[xpos,ypos]])
                xpos += 60
            color += 1
        color += 1
        xpos = 0
        ypos += 60
    return pieces

def updateScreen(screen,board):
    board.pieces = drawChess(screen,board)
    temp = Image()
    array = []
    for piece in board.pieces:
        array.append([temp.getImage(piece[0].symbol()),piece[1]])
    for img in array:
        screen.blit(img[0],img[1])

    # for img in board.pieces:
    #     screen.blit(img[0].image,img[1])


#============================MOVE=============================================
def getAvailableMove(board,position):
    kingPosition(board)
    if board.gameTiles[position[0]][position[1]].pieceOnTile.symbol != " ":
        moves = board.gameTiles[position[0]][position[1]].pieceOnTile.availableMoves(board)
        return moves
    else :
        print("Null Piece")
        return

def getMove(board):
    print("GET PLAYER MOVE : ")
    print("start : ")
    start = input()
    if board.gameTiles[board.default[start][0]][board.default[start][1]].pieceOnTile.symbol() == " ":
        print("Null Piece")
        return 9,9
    moves = getAvailableMove(board,board.default[start])
    print(moves)
    print("available moves : ",end='')
    for move in moves : 
        for key, value  in board.default.items():
            if move == value:
                print(key,end =' ')
    print("",end = '\n')
    print("end : ")
    end = input()
    for move in moves : 
        if board.default[end] == move and start != end:
            return start, end
    print("inValid Move")
    return 9,9


