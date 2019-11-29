import pygame

class Image():
	def __init__(self):
		self.WK = pygame.Surface((55,55))
		self.WK = pygame.image.load("images/WK.png")

		self.BK = pygame.Surface((55,55))
		self.BK = pygame.image.load("images/BK.png")

		self.WN = pygame.Surface((55,55))
		self.WN = pygame.image.load("images/WN.png")

		self.BN = pygame.Surface((55,55))
		self.BN = pygame.image.load("images/BN.png")

		self.BB = pygame.Surface((55,55))
		self.BB = pygame.image.load("images/BB.png")

		self.WB = pygame.Surface((55,55))
		self.WB = pygame.image.load("images/WB.png")

		self.BR = pygame.Surface((55,55))
		self.BR = pygame.image.load("images/BR.png")

		self.WR = pygame.Surface((55,55))
		self.WR = pygame.image.load("images/WR.png")

		self.BQ = pygame.Surface((55,55))
		self.BQ = pygame.image.load("images/BQ.png")

		self.WQ = pygame.Surface((55,55))
		self.WQ = pygame.image.load("images/WQ.png")

		self.BP = pygame.Surface((55,55))
		self.BP = pygame.image.load("images/BP.png")

		self.WP = pygame.Surface((55,55))
		self.WP = pygame.image.load("images/WP.png")
	def getImage(self,symbol):
		if symbol == "P":
			return self.WP
		elif symbol == "p":
			return self.BP
		elif symbol == "Q":
			return self.WQ
		elif symbol == "q":
			return self.BQ
		elif symbol == "R":
			return self.WR
		elif symbol == "r":
			return self.BR
		elif symbol == "B":
			return self.WB
		elif symbol == "b":
			return self.BB
		elif symbol == "N":
			return self.WN
		elif symbol == "n":
			return self.BN
		elif symbol == "K":
			return self.WK
		elif symbol == "k":
			return self.BK