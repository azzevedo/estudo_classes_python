class Veiculo():
	def __init__(self, possuiMotor, rodas):
		self.rodas = rodas
		self.possuiMotor = possuiMotor
		self.ligado = False
		self.andando = False

	def ligar(self):
		if not self.possuiMotor:
			self.ligarVeiculoSemMotor()
		elif self.andando or self.ligado:
			print("O veículo já está ligado")
		else:
			print("Iniciando o motor")
			self.ligado = True

	def desligar(self):
		if not self.possuiMotor:
			self.desligarVeiculoSemMotor()
		elif self.andando:
			self.parar()
			print("Desligando o motor")
			self.ligado = False
		elif self.ligado:
			print("Desligando o motor")
			self.ligado = False
		else:
			print("O veículo já está desligado")

	def andar(self):
		if not self.possuiMotor:
			self.andando = True
			print("Força nas canelas")
		elif self.andando:
			print("O veículo já está andando")
		elif self.ligado:
			self.andando = True
			print("Andando")
		else:
			self.ligar()
			self.andando = True
			print("Andando")

	def parar(self):
		if self.andando:
			print("Parando veículo")
			self.andando = False
		else:
			print("O veículo já está parado")

	def ligarVeiculoSemMotor(self):
		print("Este veículo não possui motor")
		print("Para 'ligar' basta andar")

	def desligarVeiculoSemMotor(self):
		print("Para 'desligar' basta parar")


