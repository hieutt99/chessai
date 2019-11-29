import pygame
from Pieces.Piece import Piece
class Pawn(Piece):
    def __init__(self,alliance,position):
        self.alliance = alliance
        self.point = 100*self.alliance
        # self.image = pygame.Surface((55,55))
        # self.setImage()
        self.position = position
        self.moved = False
    def symbol(self):
        return 'P' if self.alliance == 1 else 'p'
    def setImage(self):
        if(self.alliance == -1):
            self.image = pygame.image.load("images/BP.png")
        elif(self.alliance == 1):
            self.image = pygame.image.load("images/WP.png")
    def availableMoves(self,board):
        # no en passant yet
        moves = []
        if self.alliance == 1:
        #WHITE PAWN
            #pawn an quan cheo trai
            if self.position[0]-1 >= 0 and self.position[1]-1>= 0\
            and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol()!=" "\
            and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.alliance != \
                self.alliance:
                moves.append([self.position[0]-1,self.position[1]-1])
            #pawn an quan cheo phai
            if self.position[0]-1 >= 0 and self.position[1]+1 <= 7\
            and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol()!=" "\
            and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.alliance != 1:
                moves.append([self.position[0]-1,self.position[1]+1])
            #pawn bi chan thang
            if  self.position[0]-1>=0 and \
                board.gameTiles[self.position[0]-1][self.position[1]].pieceOnTile.symbol()!=" ":
                pass
            #pawn di thang 
            if self.position[0]-1 >= 0 \
            and board.gameTiles[self.position[0]-1][self.position[1]].pieceOnTile.symbol() == " ":
                moves.append([self.position[0]-1,self.position[1]])
                if self.moved == False and board.gameTiles[self.position[0]-2][self.position[1]]\
                    .pieceOnTile.symbol() == " ":
                    moves.append([self.position[0]-2,self.position[1]])
                elif self.moved == True :
                    pass
            return moves
        if self.alliance == -1 :
        #BLACK PAWN
            #pawn an quan cheo trai
            if self.position[0]+1 <=7 and self.position[1]-1 >=0\
            and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol()!=" "\
            and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.alliance != \
                self.alliance:
                moves.append([self.position[0]+1,self.position[1]-1])
            #pawn an quan cheo phai
            if self.position[0]+1 <= 7 and self.position[1]+1 <= 7\
            and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol()!=" "\
            and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.alliance != \
                self.alliance:
                moves.append([self.position[0]+1,self.position[1]+1])
            #pawn bi chan thang
            if  self.position[0]+1<=7 and \
                board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol()!=" ":
                pass
            #pawn di thang 
            if self.position[0]+1 <= 7 \
            and board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol() == " ":
                moves.append([self.position[0]+1,self.position[1]])
                if self.moved == False and board.gameTiles[self.position[0]+2][self.position[1]]\
                    .pieceOnTile.symbol() == " ":
                    moves.append([self.position[0]+2,self.position[1]])
                elif self.moved == True :
                    pass
            return moves
                    