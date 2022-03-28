from carro import Carro
from barco import Barco


class Anfibio(Carro, Barco):

	def __init__(self, velocidadeEmTerra, velocidadeEmAgua, qtdPortas, qtdHelices):
		self.velocidadeEmTerra = velocidadeEmTerra
		self.velocidadeEmAgua = velocidadeEmAgua
		self.qtdPortas = qtdPortas
		self.qtdHelices = qtdHelices

		Carro.__init__(self, velocidadeEmTerra, qtdPortas)
		Barco.__init__(self, velocidadeEmAgua, qtdHelices)
