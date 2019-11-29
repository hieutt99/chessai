import pygame
from Pieces.Piece import Piece
class Bishop(Piece):
    def __init__(self,alliance,position):
        self.alliance = alliance
        self.point = 300*self.alliance
        # self.image = pygame.Surface((55,55))
        # self.setImage()
        self.position = position
    def symbol(self):
        return 'B' if self.alliance == 1 else 'b'
    def setImage(self):
        if(self.alliance == -1):
            self.image = pygame.image.load("images/BB.png")
        elif(self.alliance == 1):
            self.image = pygame.image.load("images/WB.png")
    def availableMoves(self,board):
        moves = []
        
        if self.alliance == 1 :
            #go north - west
            count = 1
            while self.position[0] + count <= 7 and self.position[1] - count >= 0:
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+count,self.position[1]-count])
                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + count, self.position[1]-count])
                count+=1
            #go north east
            count = 1
            while self.position[0] + count <= 7 and self.position[1] + count <= 7:
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+count,self.position[1]+count])
                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + count, self.position[1]+count])
                count+=1
            #go east south
            count = 1
            while self.position[0] - count >= 0 and self.position[1] + count <= 7:
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-count,self.position[1]+count])
                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - count, self.position[1]+count])
                count+=1
            #go south west
            count = 1
            while self.position[0] - count >= 0 and self.position[1] - count >= 0:
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-count,self.position[1]-count])
                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - count, self.position[1]-count])
                count+=1
            return moves
        if self.alliance == -1 :
            #go north - west
            count = 1
            while self.position[0] + count <= 7 and self.position[1] - count >= 0:
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+count,self.position[1]-count])
                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]-count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + count, self.position[1]-count])
                count+=1
            #go north east
            count = 1
            while self.position[0] + count <= 7 and self.position[1] + count <= 7:
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+count,self.position[1]+count])
                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]+count][self.position[1]+count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + count, self.position[1]+count])
                count+=1
            #go east south
            count = 1
            while self.position[0] - count >= 0 and self.position[1] + count <= 7:
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-count,self.position[1]+count])
                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]+count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - count, self.position[1]+count])
                count+=1
            #go south west
            count = 1
            while self.position[0] - count >= 0 and self.position[1] - count >= 0:
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-count,self.position[1]-count])
                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.\
                    alliance == self.alliance:

                    break
                
                if  board.gameTiles[self.position[0]-count][self.position[1]-count].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - count, self.position[1]-count])
                count+=1
            return moves
            
