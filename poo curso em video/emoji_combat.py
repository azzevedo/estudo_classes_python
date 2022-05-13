from random import randint
'''
Lutador

- nome
- nacionalidade
- idade
- altura
- peso
- categoria
- vitorias
- derrotas
- empates

+ apresentar()
+ status()
+ ganharLuta()
+ perderLuta()
+ empatarLuta()
'''

class ILutador():
	def apresentar(self):
		raise NotImplementedError('Implementa essa buceta')

	def status(self):
		raise NotImplementedError('Implementa essa buceta')

	def ganharLuta(self):
		raise NotImplementedError('Implementa essa buceta')

	def perderLuta(self):
		raise NotImplementedError('Implementa essa buceta')

	def empatarLuta(self):
		raise NotImplementedError('Implementa essa buceta')



class Lutador(ILutador):

	def __init__(self, nome, nac, idade, altura, peso, vitorias, derrotas, empates):
		self.__nome = str
		self.__nacionalidade = str
		self.__idade = int
		self.__altura = float
		self.__peso = float
		self.__categoria = str
		self.__vitorias = int
		self.__derrotas = int
		self.__empates = int

		self.setNome(nome)
		self.setNacionalidade(nac)
		self.setIdade(idade)
		self.setAltura(altura)
		self.setPeso(peso)
		self.setVitorias(vitorias)
		self.setDerrotas(derrotas)
		self.setEmpates(empates)

	def setNome(self, nome):
		self.__nome = nome

	def getNome(self):
		return self.__nome

	def setNacionalidade(self, nac):
		self.__nacionalidade = nac

	def getNacionalidade(self):
		return self.__nacionalidade

	def setIdade(self, i):
		self.__idade = i

	def getIdade(self):
		return self.__idade

	def setAltura(self, a):
		self.__altura = a

	def getAltura(self):
		return self.__altura

	def setPeso(self, p):
		self.__peso = p
		self.__setCategoria()

	def getPeso(self):
		return self.__peso

	def __setCategoria(self):
		p = self.getPeso()

		if p < 52.2:
			tipo = 'Inválido'
		elif p <= 70.3:
			tipo = 'Leve'
		elif p <= 83.9:
			tipo = 'Médio'
		elif p <= 120.2:
			tipo = 'Pesado'
		else:
			tipo = 'Inválido'

		self.__categoria = tipo

	def getCategoria(self):
		return self.__categoria

	def setVitorias(self, v):
		self.__vitorias = v

	def getVitorias(self):
		return self.__vitorias

	def setDerrotas(self, d):
		self.__derrotas = d

	def getDerrotas(self):
		return self.__derrotas

	def setEmpates(self, e):
		self.__empates = e

	def getEmpates(self):
		return self.__empates

	def apresentar(self):
		print('AGORA NO RING!!')
		print('Lutador: ', self.getNome())
		print('Origem: ', self.getNacionalidade())
		print(self.getIdade(), 'anos')
		print(self.getAltura(), 'm de altura')
		print('Pesando: ', self.getPeso(), ' Kg')
		print('Ganhou: ', self.getVitorias())
		print('Perdeu: ', self.getDerrotas())
		print('Empatou: ', self.getEmpates())

	def status(self):
		print(self.getNome())
		print('é um peso', self.getCategoria().lower())
		print(self.getVitorias(), ' vitorias')
		print(self.getDerrotas(), ' derrotas')
		print(self.getEmpates(), ' empates')

	def ganharLuta(self):
		self.setVitorias(self.getVitorias() + 1)

	def perderLuta(self):
		self.setDerrotas(self.getDerrotas() + 1)

	def empatarLuta(self):
		self.setEmpates(self.getEmpates() + 1)



class Luta():

	__desafiado = Lutador
	__desafiante = Lutador
	__rounds = int
	__aprovada = bool
	'''
	def __init__(self):
		self.__desafiado = Lutador
		self.__desafiante = Lutador
		self.__rounds = int
		self.__aprovada = bool
	'''

	def setDesafiado(self, dd):
		self.__desafiado = dd

	def getDesafiado(self):
		return self.__desafiado

	def setDesafiante(self, df):
		self.__desafiante = df

	def getDesafiante(self):
		return self.__desafiante

	def setRounds(self, r):
		self.__rounds = r

	def getRounds(self):
		return self.__rounds

	def setAprovada(self, a):
		self.__aprovada = a

	def getAprovada(self):
		return self.__aprovada

	def marcarLuta(self, l1, l2):
		ddCat = l1.getCategoria()
		dfCat = l2.getCategoria()
		if ddCat == dfCat and l1 != l2:
			self.setAprovada(True)
			self.setDesafiado(l1)
			self.setDesafiante(l2)
		else:
			self.setAprovada(False)
			self.setDesafiado(None)
			self.setDesafiante(None)

	def lutar(self):
		if self.getAprovada():
			dd = self.getDesafiado()
			df = self.getDesafiante()
			dd.apresentar()
			df.apresentar()
			vencedor = randint(0, 2)
			if vencedor == 0:
				print('Empate')
				dd.empatarLuta()
				df.empatarLuta()
			elif vencedor == 1:
				print(dd.getNome(), ' venceu!')
				dd.ganharLuta()
				df.perderLuta()
			else:
				print(df.getNome(), ' venceu!')
				df.ganharLuta()
				dd.perderLuta()
		else:
			print('Luta não pode acontecer')




# Lista de lutadores
l = []

l.append(Lutador('Pretty Boy', 'França', 31, 1.75, 68.9, 11, 2, 1))
l.append(Lutador('Putscript', 'Brasil', 29, 1.68, 57.8, 14, 2, 3))
l.append(Lutador('Snapshadow', 'EUA', 35, 1.65, 80.9, 5, 8, 1))
l.append(Lutador('Dead Code', 'Austrália', 28, 1.93, 91.6, 13, 0, 2))
l.append(Lutador('Ufocobol', 'Brasil', 37, 1.70, 110.3, 15, 4, 3))
l.append(Lutador('Nerdaard', 'EUA', 30, 1.81, 105.7, 3, 2, 6))



UEC01 = Luta()
UEC01.marcarLuta(l[0], l[1])
UEC01.lutar()






