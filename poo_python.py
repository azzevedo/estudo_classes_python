class Estante():

	def __init__(self):
		self.nDoc = None

	def getNDoc(self):
		return self.nDoc

	def setNDoc(self, n):
		self.nDoc = n


e = Estante()
e.setNDoc(3)
e.getNDoc()


class Caneta():

	def __init__(self, modelo, cor, ponta):
		self.modelo = ''
		self.cor = ''
		self.__ponta = 0.0
		self.setModelo(modelo)
		self.setCor(cor)
		self.setPonta(ponta)

	def setModelo(self, mod):
		self.modelo = mod

	def getModelo(self):
		return self.modelo

	def setCor(self, cor):
		self.cor = cor

	def getCor(self):
		return self.cor

	def setPonta(self, pon):
		self.__ponta = pon

	def getPonta(self):
		return self.__ponta

bic = Caneta('Bic', 'Azul', 0.7)
print(bic.getModelo())
print(bic.getPonta())


print('################')
print('################')
print('################')
print('################')
class ContaBanco():

	def __init__(self, num, tipo, dono):
		self.numConta = int
		self._tipoConta = str
		self.__dono = str
		self.__saldo = float
		self.__status = bool

		self.setNumConta(num)
		self.setTipoConta(tipo)
		self.setDono(dono)
		self.setSaldo(0)
		self.setStatus(False)

	def setStatus(self, status):
		self.__status = status

	def getStatus(self):
		return self.__status
	
	def setSaldo(self, valor):
		self.__saldo = valor

	def getSaldo(self):
		return self.__saldo

	def setDono(self, nomeDono):
		self.__dono = nomeDono

	def getDono(self):
		return self.__dono

	def setNumConta(self, nConta):
		self.numConta = nConta

	def getNumConta(self):
		return self.numConta

	def setTipoConta(self, tipoC):
		self._tipoConta = tipoC

	def getTipoConta(self):
		return self._tipoConta

	def abrirConta(self):
		self.setStatus(True)
		tipoC = self.getTipoConta()

		if tipoC == 'cc':
			self.depositar(50.0)
		elif tipoC == 'cp':
			self.depositar(150.0)

	def fecharConta(self):
		saldo = self.getSaldo()
		status = self.getStatus()

		if saldo < 0:
			print(f'Pague sua dívida de R$ {saldo:.2f} antes de fechar a conta')
		elif saldo > 0:
			print('Saque seu dinheiro antes de fechar a conta')
			self.mostrarSaldo()
		else:
			self.setStatus(False)
			print(f'Nome: {self.getDono()}')
			print(f'Conta {self.getNumConta()} fechada com sucesso!')

	def depositar(self, valor):
		status = self.getStatus()
		saldo = self.getSaldo()
		if status:
			saldo += valor
			self.setSaldo(saldo)
		else:
			print('Não pode depositar numa conta fechada')

	def sacar(self, valor):
		status = self.getStatus()
		saldo = self.getSaldo()

		if status:
			if saldo > valor:
				saldo -= valor
				self.setSaldo(saldo)
			else:
				print('Saldo insuficiente')
				self.mostrarSaldo()
		else:
			print('Não pode sacar de uma conta fechada')

	def pagarMensalidade(self):
		tipo = self.getTipoConta()
		saldo = self.getSaldo()
		if tipo == 'cc':
			taxa = 12.0
		elif tipo == 'cp':
			taxa = 20.0

		if self.getStatus():
			if saldo > taxa:
				saldo -= taxa
				self.setSaldo(saldo)
				print(f'Mensalidade de R$ {taxa:.2f} debitada com sucesso')
				self.mostrarSaldo()
			else:
				print('Saldo insuficiente para pagar mensalidade')
		else:
			print('Conta inativa não paga mensalidade')

	def mostrarSaldo(self):
		print(f'Saldo de {self.getDono()}')
		print(f'R$ {self.getSaldo():.2f}')


jubileu = ContaBanco(134, 'cc', 'Jubileu')
creusa = ContaBanco(824, 'cp', 'Creusa')

jubileu.abrirConta()
creusa.abrirConta()
jubileu.mostrarSaldo()
creusa.mostrarSaldo()



'''
# ENCAPSULAMENTO
# Metodos abstratos sao previstos mas nao implementados
## Interface soh tem metodos
# Na interface todos os metodos sao publicos
Controlador

ligar()
desligar()
abrirMenu()
fecharMenu()
maisVolume()
menosVolume()
ligarMudo()
desligarMudo()
play()
pause()


## Ao encapsular, temos que tornar todos os atributos privados
## ou protegidos mas NUNCA publicos
## A classe IMPLEMENTA a INTERFACE
## Heranca
# Classe
ControleRemoto
# Atributos
- volume
- ligado
- tocando
# Metodos
## Todos os metodos da interface vem aqui
# Metodos adicionais
- setVolume()
- getVolume()
- setLigado()
- getLigado()
- setTocando()
- getTocando()
'''

class Controlador:
	
	def ligar(): # public abstract method ligar()
		pass

	def desligar():
		pass

	def abrirMenu():
		pass
	
	def fecharMenu():
		pass

	def maisVolume():
		pass

	def menosVolume():
		pass

	def ligarMudo():
		pass

	def desligarMudo():
		pass

	def play():
		pass

	def pause():
		pass



# ControleRomote implements Controlador
class ControleRemoto(Controlador):

	def __init__(self):
		self.__volume = 50
		self.__ligado = False
		self.__tocando = False
		self.__volumeAntesMudo = 0

	def setVolume(self, v):
		self.__volume = v

	def getVolume(self):
		return self.__volume

	def setLigado(self, l):
		self.__ligado = l

	def getLigado(self):
		return self.__ligado

	def setTocando(self, t):
		self.__tocando = t

	def getTocando(self):
		return self.__tocando

	def ligar(self):
		self.setLigado(True)

	def desligar(self):
		self.setLigado(False)

	def abrirMenu(self):
		if self.getLigado():
			print('=== Menu ===')
			print(self.getLigado())
			print(self.getVolume(), end=' ')
			for i in range(0, self.getVolume(), 10):
				print('|', end='')
			print()
			print(self.getTocando())

	def fecharMenu(self):
		print('Menu fechado')

	def maisVolume(self):
		if self.getLigado():
			self.setVolume(self.getVolume() + 1)

	def menosVolume(self):
		if self.getLigado():
			self.setVolume(self.getVolume() - 1)

	# SET
	def setVolumeAntesMudo(self, v):
		self.__volumeAntesMudo = v

	# GET
	def getVolumeAntesMudo(self):
		return self.__volumeAntesMudo

	def ligarMudo(self):
		if self.getLigado():
			self.setVolumeAntesMudo(self.getVolume())
			self.setVolume(0)

	def desligarMudo(self):
		if self.getLigado():
			self.setVolume(self.getVolumeAntesMudo())

	def play(self):
		if (self.getLigado() and not self.getTocando()):
			self.setTocando(True)

	def pause(self):
		if self.getLigado() and self.getTocando():
			self.setTocando(False)


controle = ControleRemoto()
controle.ligar()
controle.abrirMenu()
controle.ligarMudo()
controle.abrirMenu()
controle.desligarMudo()
controle.abrirMenu()

