#!/usr/bin/python3

# classe abstrata
class Pessoa:
	# Também tem os setters e getters
	__nome = str
	__idade = int
	__sexo = str

	def setNome(self, nome):
		self.__nome = nome

	def getNome(self):
		return self.__nome

	def setIdade(self, idade):
		self.__idade = idade

	def getIdade(self):
		return self.__idade

	def setSexo(self, s):
		self.__sexo = s

	def getSexo(self):
		return self.__sexo

	# Metodo final (não pode ser sobrescrito)
	def fazer_aniversario():
		self.__idade += 1

	def __str__(self):
		return f'Nome: {self.__nome}\n' \
				f'Idade: {self.__idade}\n' \
				f'Sexo: {self.__sexo}'



class Visitante(Pessoa):
	"""
	Herança para implementação
	Para implementar uma classe abstrata
	Não adiciona novos métodos ou atributos
	"""
	pass



class Aluno(Pessoa):
	"""
	Herança para diferença
	Implementar e adicionar atributos e/ou métodos
	
	Também tem os setters e getters
	"""
	__matricula = int
	__curso = str

	def getMatricula(self):
		return self.__matricula

	def setMatricula(self, m):
		self.__matricula = m

	def getCurso(self):
		return self.__curso

	def setCurso(self, c):
		self.__curso = c

	def pagar_mensalidade(self):
		print('Pagando mensalidade da(o) aluna(o)', self.getNome())



class Bolsista(Aluno):
	__bolsa = float

	def setBolsa(self, bolsa):
		self.__bolsa = bolsa

	def getBolsa(self):
		return self.__bolsa

	def renovar_bolsa(self):
		print('Renovando bolsa de', self.getNome())

	# Sobreposição
	def pagar_mensalidade(self):
		print('Pagando mensalidade da(o) bolsista', self.getNome())



class Tecnico(Aluno):
	
	__registro_profissional = int

	def setRegistro(self, registro):
		self.__registro_profissional = registro

	def getRegistro(self):
		return self.__registro_profissional

	def praticar(self):
		print('Hora de por em prática o aprendizado')



class Professor(Pessoa):
	__especialidade = str
	__salario = float

	# def __init__(self, nome, idade, sexo):
	# 	super().__init__(self, nome, idade, sexo)

	def getEspecialidade(self):
		return self.__especialidade

	def setEspecialidade(self, esp):
		self.__especialidade = esp

	def getSalario(self):
		return self.__salario

	def setSalario(self, salario):
		self.__salario = salario

	def receberAum(self, aum):
		self.__salario += aum





v1 = Visitante()
v1.setNome('Celestino')
v1.setIdade(22)
v1.setSexo('M')
print(v1)


a1 = Aluno()
a1.setNome('Roberta')
a1.setMatricula(1010)
a1.setCurso('POO')
a1.setIdade(42)
a1.setSexo('F')
print(a1)
a1.pagar_mensalidade()

b1 = Bolsista()
b1.setNome('Marcela')
b1.setIdade('30')
b1.setSexo('F')
b1.setMatricula(1011)
b1.setBolsa(13.5)
b1.renovar_bolsa()
b1.pagar_mensalidade()
print(b1)

p1 = Professor()
p1.setNome('Guanabara')
p1.setIdade(90)
p1.setSexo('M')
p1.setSalario(5673.62)
p1.setEspecialidade('Informática')
p1.receberAum(63045.02)
print(p1)

