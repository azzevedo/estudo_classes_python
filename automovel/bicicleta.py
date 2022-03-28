from veiculos import Veiculo

class Bicicleta(Veiculo):
	possuiGuidao = True
	def __init__(self, qtdRodas):
		super().__init__(False, qtdRodas)
		
	def empinar(self):
		print("Empinando a bicicleta")