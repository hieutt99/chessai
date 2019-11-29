import pygame
from Pieces.King import King 
import settings
import sys
from Board.board import Board
import copy
import bot

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Chess Python")
board = Board()

def run_game():
    board.createBoard()
    board.printBoard()
    settings.updateScreen(screen,board)
    pygame.display.flip()

    # while not board.end_game:
    #     x,y = settings.getMove(board)
    #     while(x == 9 and y == 9):
    #         x,y = settings.getMove(board)
    #     board.updateMove(x,y)
    #     board.printBoard()
    #     settings.updateScreen(screen,board)
    #     settings.check_events(screen,board)
    #     pygame.display.flip()
    while not board.end_game:
        # for i in range(8):
        #     for j in range(8):
        #         print(board.gameTiles[i][j].pos)
        
        if board.turn == 1:
            settings.check_events(screen,board)
        elif board.turn == -1 :
            print("Black bot turn...")
            tree = bot.createTree(board)
            start,end = bot.moveOfBot(board,tree)
            if (start == None or end == None):
                print("Error in bot move so end game...")
                break
            print(start+end)
            # print("dang update")
            board.updateMove(start,end)
            # print("da update")
            settings.updateScreen(screen,board)
            # bot.checkEndGame(board)
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
            print("Black bot turn over, Board Analysis : "+str(board.evaluation))
            board.printBoard()
            del(tree)
        # settings.check_events(screen,board)
        pygame.display.flip()
    print("End Game !")
    input()
    # temp = King(1,[0,4])
    # temptemp = copy.deepcopy(temp)
run_game()