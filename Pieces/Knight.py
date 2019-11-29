import pygame
from Pieces.Piece import Piece

class Knight(Piece):

    def __init__(self,alliance,position):
        self.alliance = alliance
        self.point = 300*self.alliance
        # self.image = pygame.Surface((55,55))
        # self.setImage()
        self.position = position
    def symbol(self):
        return 'N' if self.alliance == 1 else 'n'
    def setImage(self):
        if(self.alliance == -1):
            self.image = pygame.image.load("images/BN.png")
        elif(self.alliance == 1):
            self.image = pygame.image.load("images/WN.png")
    def availableMoves(self, board):
        moves = []
        # print(self.position)
        if self.alliance == 1 :
            
            if  self.position[0]+2 <= 7 and self.position[1]-1 >= 0 and \
                ((board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]+2,self.position[1]-1])
            
            if  self.position[0]+1 <= 7 and self.position[1]-2 >= 0 and\
                ((board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]+1,self.position[1]-2])
            
            if  self.position[0]+2 <= 7 and self.position[1]+1 <= 7 and\
                ((board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]+2,self.position[1]+1])
            
            if  self.position[0]+1 <=7 and self.position[1]+2 <=7 and\
                ((board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]+1,self.position[1]+2])

            if  self.position[0]-1 >= 0 and self.position[1]-2 >= 0 and\
                ((board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-1,self.position[1]-2])
            
            if  self.position[0]-2 >=0 and self.position[1]-1 >= 0 and\
                ((board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]-2,self.position[1]-1])
            
            if  self.position[0]-2 >=0 and self.position[1]+1 <=7 and\
                ((board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-2,self.position[1]+1])
            
            if  self.position[0]-1 >= 0 and self.position[1]+2 <=7 and\
                ((board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-1,self.position[1]+2])
            
            return moves
        if self.alliance == -1 :
            
            if  self.position[0]+2 <= 7 and self.position[1]-1 >= 0 and \
                ((board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+2][self.position[1]-1].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]+2,self.position[1]-1])
            
            if  self.position[0]+1 <= 7 and self.position[1]-2 >= 0 and\
                ((board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+1][self.position[1]-2].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]+1,self.position[1]-2])
            
            if  self.position[0]+2 <= 7 and self.position[1]+1 <= 7 and\
                ((board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+2][self.position[1]+1].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]+2,self.position[1]+1])
            
            if  self.position[0]+1 <=7 and self.position[1]+2 <=7 and\
                ((board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]+1][self.position[1]+2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]+1,self.position[1]+2])

            if  self.position[0]-1 >= 0 and self.position[1]-2 >= 0 and\
                ((board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-1][self.position[1]-2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-1,self.position[1]-2])
            
            if  self.position[0]-2 >=0 and self.position[1]-1 >= 0 and\
                ((board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-2][self.position[1]-1].pieceOnTile.symbol() == " ")):
                
                moves.append([self.position[0]-2,self.position[1]-1])
            
            if  self.position[0]-2 >=0 and self.position[1]+1 <=7 and\
                ((board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-2][self.position[1]+1].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-2,self.position[1]+1])
            
            if  self.position[0]-1 >= 0 and self.position[1]+2 <=7 and\
                ((board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.symbol() != " " and\
                board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.alliance != self.alliance) or\
                (board.gameTiles[self.position[0]-1][self.position[1]+2].pieceOnTile.symbol() == " ")):

                moves.append([self.position[0]-1,self.position[1]+2])
            
            return moves
