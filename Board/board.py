import pygame
from Board.tile import Tile
from Pieces.NullPiece import NullPiece
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.King import King
#rook = 50 - r
#knight = 30 - k
#bishop = 30 - b
#king = 900 - k
#queen = 90 - q
#pawn = 10 - p
class Board():
    default = {
        "8a":[0,0],"8b":[0,1],"8c":[0,2],"8d":[0,3],"8e":[0,4],"8f":[0,5],"8g":[0,6],"8h":[0,7],
        "7a":[1,0],"7b":[1,1],"7c":[1,2],"7d":[1,3],"7e":[1,4],"7f":[1,5],"7g":[1,6],"7h":[1,7],
        "6a":[2,0],"6b":[2,1],"6c":[2,2],"6d":[2,3],"6e":[2,4],"6f":[2,5],"6g":[2,6],"6h":[2,7],
        "5a":[3,0],"5b":[3,1],"5c":[3,2],"5d":[3,3],"5e":[3,4],"5f":[3,5],"5g":[3,6],"5h":[3,7],
        "4a":[4,0],"4b":[4,1],"4c":[4,2],"4d":[4,3],"4e":[4,4],"4f":[4,5],"4g":[4,6],"4h":[4,7],
        "3a":[5,0],"3b":[5,1],"3c":[5,2],"3d":[5,3],"3e":[5,4],"3f":[5,5],"3g":[5,6],"3h":[5,7],
        "2a":[6,0],"2b":[6,1],"2c":[6,2],"2d":[6,3],"2e":[6,4],"2f":[6,5],"2g":[6,6],"2h":[6,7],
        "1a":[7,0],"1b":[7,1],"1c":[7,2],"1d":[7,3],"1e":[7,4],"1f":[7,5],"1g":[7,6],"1h":[7,7]
    }
    def __init__(self):
        self.default = {
        "8a":[0,0],"8b":[0,1],"8c":[0,2],"8d":[0,3],"8e":[0,4],"8f":[0,5],"8g":[0,6],"8h":[0,7],
        "7a":[1,0],"7b":[1,1],"7c":[1,2],"7d":[1,3],"7e":[1,4],"7f":[1,5],"7g":[1,6],"7h":[1,7],
        "6a":[2,0],"6b":[2,1],"6c":[2,2],"6d":[2,3],"6e":[2,4],"6f":[2,5],"6g":[2,6],"6h":[2,7],
        "5a":[3,0],"5b":[3,1],"5c":[3,2],"5d":[3,3],"5e":[3,4],"5f":[3,5],"5g":[3,6],"5h":[3,7],
        "4a":[4,0],"4b":[4,1],"4c":[4,2],"4d":[4,3],"4e":[4,4],"4f":[4,5],"4g":[4,6],"4h":[4,7],
        "3a":[5,0],"3b":[5,1],"3c":[5,2],"3d":[5,3],"3e":[5,4],"3f":[5,5],"3g":[5,6],"3h":[5,7],
        "2a":[6,0],"2b":[6,1],"2c":[6,2],"2d":[6,3],"2e":[6,4],"2f":[6,5],"2g":[6,6],"2h":[6,7],
        "1a":[7,0],"1b":[7,1],"1c":[7,2],"1d":[7,3],"1e":[7,4],"1f":[7,5],"1g":[7,6],"1h":[7,7]
        }
        temp = Tile([0,0],NullPiece([0,0]))
        self.gameTiles = [[temp for j in range(8)] for _ in range(8)] 
        self.pieces = []

        self.turn = 0
        self.end_game = False

        self.selectedStartTile = Tile([],NullPiece([]))
        self.selectedEndTile = Tile([],NullPiece([]))
        self.mx = 0
        self.my = 0
        self.start = ""
        self.end = ""
        self.legalMoves = []

        self.evaluation = 0
        self.movesForBot = []

        #so luot di 
        self.number = 0

        #==========King=======================
        self.whiteKing = [7,4]
        self.blackKing = [0,4]
    def createBoard(self):
        print("starting a new game ....")
        # self.status = {
        #     "8a":"r","8b":"n","8c":"b","8d":"k","8e":"q","8f":"b","8g":"n","8h":"r",
        #     "7a":"p","7b":"p","7c":"p","7d":"p","7e":"p","7f":"p","7g":"p","7h":"p",
        #     "6a":" ","6b":" ","6c":" ","6d":" ","6e":" ","6f":" ","6g":" ","6h":" ",
        #     "5a":" ","5b":" ","5c":" ","5d":" ","5e":" ","5f":" ","5g":" ","5h":" ",
        #     "4a":" ","4b":" ","4c":" ","4d":" ","4e":" ","4f":" ","4g":" ","4h":" ",
        #     "3a":" ","3b":" ","3c":" ","3d":" ","3e":" ","3f":" ","3g":" ","3h":" ",
        #     "2a":"P","2b":"P","2c":"P","2d":"P","2e":"P","2f":"P","2g":"P","2h":"P",
        #     "1a":"R","1b":"N","1c":"B","1d":"K","1e":"Q","1f":"B","1g":"N","1h":"R"
        # }
        for i in range(8):
            for j in range(8):
                self.gameTiles[i][j] = Tile([i,j],NullPiece([0,0]))
        self.gameTiles[0][0] = Tile([0,0], Rook(-1, [0,0]))
        self.gameTiles[0][1] = Tile([0,1], Knight(-1, [0,1]))
        self.gameTiles[0][2] = Tile([0,2], Bishop(-1, [0,2]))
        self.gameTiles[0][3] = Tile([0,3], Queen(-1, [0,3]))
        self.gameTiles[0][4] = Tile([0,4], King(-1, [0,4]))
        self.gameTiles[0][5] = Tile([0,5], Bishop(-1, [0,5]))
        self.gameTiles[0][6] = Tile([0,6], Knight(-1, [0,6]))
        self.gameTiles[0][7] = Tile([0,7], Rook(-1, [0,7]))
        self.gameTiles[1][0] = Tile([1,0], Pawn(-1, [1,0]))
        self.gameTiles[1][1] = Tile([1,1], Pawn(-1, [1,1]))
        self.gameTiles[1][2] = Tile([1,2], Pawn(-1, [1,2]))
        self.gameTiles[1][3] = Tile([1,3], Pawn(-1, [1,3]))
        self.gameTiles[1][4] = Tile([1,4], Pawn(-1, [1,4]))
        self.gameTiles[1][5] = Tile([1,5], Pawn(-1, [1,5]))
        self.gameTiles[1][6] = Tile([1,6], Pawn(-1, [1,6]))
        self.gameTiles[1][7] = Tile([1,7], Pawn(-1, [1,7]))

        self.gameTiles[6][0] = Tile([6,0], Pawn(1, [6,0]))
        self.gameTiles[6][1] = Tile([6,1], Pawn(1, [6,1]))
        self.gameTiles[6][2] = Tile([6,2], Pawn(1, [6,2]))
        self.gameTiles[6][3] = Tile([6,3], Pawn(1, [6,3]))
        self.gameTiles[6][4] = Tile([6,4], Pawn(1, [6,4]))
        self.gameTiles[6][5] = Tile([6,5], Pawn(1, [6,5]))
        self.gameTiles[6][6] = Tile([6,6], Pawn(1, [6,6]))
        self.gameTiles[6][7] = Tile([6,7], Pawn(1, [6,7]))
        self.gameTiles[7][0] = Tile([7,0], Rook(1, [7,0]))
        self.gameTiles[7][1] = Tile([7,1], Knight(1, [7,1]))
        self.gameTiles[7][2] = Tile([7,2], Bishop(1, [7,2]))
        self.gameTiles[7][3] = Tile([7,3], Queen(1, [7,3]))
        self.gameTiles[7][4] = Tile([7,4], King(1, [7,4]))
        self.gameTiles[7][5] = Tile([7,5], Bishop(1, [7,5]))
        self.gameTiles[7][6] = Tile([7,6], Knight(1, [7,6]))
        self.gameTiles[7][7] = Tile([7,7], Rook(1, [7,7]))
        
        #White make the first move
        self.turn = 1


    def printBoard(self):
        count = 0
        print("=====================================")
        print("  A|B|C|D|E|F|G|H")
        print("-------------------------------------")
        for x in range(8):
            print(str(8-x),end="")
            for y in range(8):
                print('|'+ self.gameTiles[x][y].pieceOnTile.symbol(),end = '')
            print('|',end = '\n')
        print("=====================================")

    def castling(self,start, end):
        move = self.default
        #WHITE KING
        if  self.gameTiles[move[start][0]][move[start][1]].pieceOnTile.alliance == 1 :
            #CASTLING RIGHT 
            if end == "1g":
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]].pieceOnTile
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.castle = True
                self.gameTiles[move[start][0]][move[start][1]].pieceOnTile = NullPiece(move[start])
                self.gameTiles[move[start][0]][move[start][1]+1].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]+3].pieceOnTile
                self.gameTiles[move[start][0]][move[start][1]+3].pieceOnTile = NullPiece([
                    move[start][0],move[start][1]+3])
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.position = move[end]
                self.gameTiles[move[start][0]][move[start][1]+1].pieceOnTile.position = \
                    [move[start][0],move[start][1]+1]
            #CASTLING LEFT
            elif end == "1c":
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]].pieceOnTile
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.castle = True
                self.gameTiles[move[start][0]][move[start][1]].pieceOnTile = NullPiece(move[start])
                self.gameTiles[move[start][0]][move[start][1]-1].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]-4].pieceOnTile
                self.gameTiles[move[start][0]][move[start][1]-4].pieceOnTile = NullPiece([
                    move[start][0],move[start][1]-4])
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.position = move[end]
                self.gameTiles[move[start][0]][move[start][1]-1].pieceOnTile.position = \
                    [move[start][0],move[start][1]-1]
        #BLACK KING
        elif self.gameTiles[move[start][0]][move[start][1]].pieceOnTile.alliance == -1 :
            #CASTLING RIGHT 
            if end == "8g":
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]].pieceOnTile
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.castle = True
                self.gameTiles[move[start][0]][move[start][1]].pieceOnTile = NullPiece(move[start])
                self.gameTiles[move[start][0]][move[start][1]+1].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]+3].pieceOnTile
                self.gameTiles[move[start][0]][move[start][1]+3].pieceOnTile = NullPiece([
                    move[start][0],move[start][1]+3])
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.position = move[end]
                self.gameTiles[move[start][0]][move[start][1]+1].pieceOnTile.position = \
                    [move[start][0],move[start][1]+1]
            #CASTLING LEFT
            elif end == "8c":
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]].pieceOnTile
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.castle = True
                self.gameTiles[move[start][0]][move[start][1]].pieceOnTile = NullPiece(move[start])
                self.gameTiles[move[start][0]][move[start][1]-1].pieceOnTile = self.gameTiles\
                    [move[start][0]][move[start][1]-4].pieceOnTile
                self.gameTiles[move[start][0]][move[start][1]-4].pieceOnTile = NullPiece([
                    move[start][0],move[start][1]-4])  
                self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.position = move[end]
                self.gameTiles[move[start][0]][move[start][1]-1].pieceOnTile.position = \
                    [move[start][0],move[start][1]-1]  
    def updateMove(self,start,end):
        move = self.default
        if  (self.gameTiles[move[start][0]][move[start][1]].pieceOnTile.symbol() == "K" and\
                start == "1e" and (end == "1c" or end == "1g")) or\
            (self.gameTiles[move[start][0]][move[start][1]].pieceOnTile.symbol() == "k" and\
                start == "8e" and (end == "8c" or end == "8g")):
            self.castling(start,end)
            # if self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == "K" or \
            #     self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == "k":
            #     self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
            #     self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.castle = True 
        else :
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile = \
                self.gameTiles[move[start][0]][move[start][1]].pieceOnTile
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.position = move[end]
            self.gameTiles[move[start][0]][move[start][1]].pieceOnTile = NullPiece(move[start])
        if  self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'p' or \
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'P' or \
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'K' or \
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'k' or \
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'R' or \
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.symbol() == 'r':
            self.gameTiles[move[end][0]][move[end][1]].pieceOnTile.moved = True
        
        #change turn 
        # if self.turn == 1 :
        #     print("White made a move : ", end = "" )
        # else :
        #     print("Black made a move : ", end = "")
        self.turn = -(self.turn)
        self.number += 1
    def updatePieceForCheck(self):
        self.pieces = []
        for i in range(8):
            for j in range(8):
                if self.gameTiles[i][j].pieceOnTile.symbol() != " ":
                    self.pieces.append([self.gameTiles[i][j].pieceOnTile,[0,0]])
    



 