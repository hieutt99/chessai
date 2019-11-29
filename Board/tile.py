class Tile:
    pieceOnTile = None
    tileCoordinate = []

    def __init__(self,coordinate ,piece):
        self.pos = []
        self.tileCoordinate = coordinate
        self.pieceOnTile = piece