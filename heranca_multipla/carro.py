from terrestre import Terrestre

class Carro(Terrestre):

	rodas = 4

	def __init__(self, velocidadeEmTerra, qtdPortas, **kwargs):
		self.qtdPortas = qtdPortas
		super().__init__(velocidadeEmTerra)