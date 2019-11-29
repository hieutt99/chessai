import pygame
from Pieces.Piece import Piece

class King(Piece):
    def __init__(self,alliance,position):
        self.alliance = alliance
        self.point = 9000*self.alliance
        # self.image = pygame.Surface((55,55))
        # self.setImage()
        self.position = position
        self.moved = False
        self.castle = False
        self.check = False
    def symbol(self):
        return 'K' if self.alliance == 1 else 'k'
    def setImage(self):
        if(self.alliance == -1):
            self.image = pygame.image.load("images/BK.png")
        elif(self.alliance == 1):
            self.image = pygame.image.load("images/WK.png")
    def availableMoves(self,board):
        moves = []
        if self.alliance == 1 :
            # go southern
            if   self.position[0] + 1 <= 7 :
                if  board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0]+1,self.position[1]])
                if  board.gameTiles[self.position[0] + 1][self.position[1]].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0] + 1][self.position[1]].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0]+1,self.position[1]])
            # go northern
            if   self.position[0] - 1 >= 0 :
                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0] - 1,self.position[1]])

                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1,self.position[1]])
            # go west 
            if   self.position[1] - 1 >= 0 :
                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0],self.position[1] - 1])

                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0],self.position[1] - 1])
            #go east
            if   self.position[1] + 1 <= 7 :
                if  board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0],self.position[1] + 1])

                if  board.gameTiles[self.position[0]][self.position[1]+ 1].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0]][self.position[1]+1].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0],self.position[1] + 1])

            #go north - west
            if self.position[0] + 1 <= 7 and self.position[1] - 1 >= 0:
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+1,self.position[1]-1])
                
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + 1, self.position[1]-1])
            #go north east
            if self.position[0] + 1 <= 7 and self.position[1] + 1 <= 7:
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+1,self.position[1]+1])
                
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + 1, self.position[1]+1])
            #go east south
            if self.position[0] - 1 >= 0 and self.position[1] + 1 <= 7:
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-1,self.position[1]+1])
                
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1, self.position[1]+1])
            
            #go south west
            if self.position[0] - 1 >= 0 and self.position[1] - 1 >= 0:
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-1,self.position[1]-1])
                
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1, self.position[1]-1])
                
            #CASTLING RIGHT
            if  self.moved == False and board.gameTiles[self.position[0]][self.position[1]+1].pieceOnTile.\
                symbol() == " " and board.gameTiles[self.position[0]][self.position[1]+2].pieceOnTile.symbol()\
                == " " and board.gameTiles[self.position[0]][self.position[1]+3].pieceOnTile.symbol() == "R" and\
                board.gameTiles[self.position[0]][self.position[1]+3].pieceOnTile.moved == False and\
                self.check == False :

                moves.append([self.position[0],self.position[1]+2])
            #CASTLING LEFT
            if  self.moved == False and board.gameTiles[self.position[0]][self.position[1]-1].pieceOnTile.\
                symbol() == " " and board.gameTiles[self.position[0]][self.position[1]-2].pieceOnTile.symbol()\
                == " " and board. gameTiles[self.position[0]][self.position[1]-3].pieceOnTile.symbol() == " "and \
                board.gameTiles[self.position[0]][self.position[1]-4].pieceOnTile.symbol() == "R" and\
                board.gameTiles[self.position[0]][self.position[1]-4].pieceOnTile.moved == False and\
                self.check == False:

                moves.append([self.position[0],self.position[1]-2])
            return moves
        if self.alliance == -1 :
            # go southern
            if   self.position[0] + 1 <= 7 :
                if  board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0]+1,self.position[1]])
                if  board.gameTiles[self.position[0] + 1][self.position[1]].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0] + 1][self.position[1]].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]+1][self.position[1]].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0]+1,self.position[1]])
            # go northern
            if   self.position[0] - 1 >= 0 :
                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0] - 1,self.position[1]])

                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0] - 1][self.position[1]].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1,self.position[1]])
            # go west 
            if   self.position[1] - 1 >= 0 :
                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0],self.position[1] - 1])

                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]][self.position[1] - 1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0],self.position[1] - 1])
            #go east
            if   self.position[1] + 1 <= 7 :
                if  board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile.symbol()\
                    != " " and board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile\
                    .alliance != self.alliance :
                    
                    moves.append([self.position[0],self.position[1] + 1])

                if  board.gameTiles[self.position[0]][self.position[1]+ 1].pieceOnTile.symbol() != " "\
                    and board.gameTiles[self.position[0]][self.position[1]+1].pieceOnTile.alliance \
                    == self.alliance :
                    
                    pass
                if  board.gameTiles[self.position[0]][self.position[1] + 1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0],self.position[1] + 1])

            #go north - west
            if self.position[0] + 1 <= 7 and self.position[1] - 1 >= 0:
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+1,self.position[1]-1])
                
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]+1][self.position[1]-1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + 1, self.position[1]-1])
            #go north east
            if self.position[0] + 1 <= 7 and self.position[1] + 1 <= 7:
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]+1,self.position[1]+1])
                
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]+1][self.position[1]+1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] + 1, self.position[1]+1])
            #go east south
            if self.position[0] - 1 >= 0 and self.position[1] + 1 <= 7:
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-1,self.position[1]+1])
                
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]-1][self.position[1]+1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1, self.position[1]+1])
            
            #go south west
            if self.position[0] - 1 >= 0 and self.position[1] - 1 >= 0:
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol() \
                    != " " and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.\
                    alliance != self.alliance :

                    moves.append([self.position[0]-1,self.position[1]-1])
                
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol() \
                    != " "  and board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.\
                    alliance == self.alliance:

                    pass
                
                if  board.gameTiles[self.position[0]-1][self.position[1]-1].pieceOnTile.symbol()\
                    == " ":

                    moves.append([self.position[0] - 1, self.position[1]-1])
            #CASTLING RIGHT
            if  self.moved == False and board.gameTiles[self.position[0]][self.position[1]+1].pieceOnTile.\
                symbol() == " " and board.gameTiles[self.position[0]][self.position[1]+2].pieceOnTile.symbol()\
                == " " and board.gameTiles[self.position[0]][self.position[1]+3].pieceOnTile.symbol() == "r"\
                and board.gameTiles[self.position[0]][self.position[1]+3].pieceOnTile.moved == False and\
                self.check == False:

                moves.append([self.position[0],self.position[1]+2])
            #CASTLING LEFT
            if  self.moved == False and board.gameTiles[self.position[0]][self.position[1]-1].pieceOnTile.\
                symbol() == " " and board.gameTiles[self.position[0]][self.position[1]-2].pieceOnTile.symbol()\
                == " " and board. gameTiles[self.position[0]][self.position[1]-3].pieceOnTile.symbol() == " "and \
                board.gameTiles[self.position[0]][self.position[1]-4].pieceOnTile.symbol() == "r" and\
                board.gameTiles[self.position[0]][self.position[1]-4].pieceOnTile.moved == False and\
                self.check == False:

                moves.append([self.position[0],self.position[1]-2])
            return moves