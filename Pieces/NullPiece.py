from Pieces.Piece import Piece
class NullPiece(Piece):

    def __init__(self,position):
        self.position = position
        self.point = 0
        self.alliance = 0
        pass
    def symbol(self):
        return " "
