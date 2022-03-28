from veiculos import Veiculo

class Carro(Veiculo):
	def __init__(self, qtdRodas):
		super().__init__(True, qtdRodas)