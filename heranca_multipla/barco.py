from aquatico import Aquatico

class Barco(Aquatico):

	def __init__(self, velocidadeEmAgua, qtdHelices):
		self.qtdHelices = qtdHelices
		super().__init__(velocidadeEmAgua)
