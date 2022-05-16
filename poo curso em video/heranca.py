#!/usr/bin/python3

""" Herança """



class Pessoa:
	__nome = __sexo = str
	__idade = int

	# def __init__(sefl, nome, idade, sexo):
	# 	self.__nome = nome
	# 	self.__idade = idade
	# 	self.__sexo = sexo

	def getNome(self):
		return self.__nome

	def setNome(self, nome):
		self.__nome = nome

	def getSexo(self):
		return self.__sexo

	def setSexo(self, sexo):
		self.__sexo = sexo

	def getIdade(self):
		return self.__idade

	def setIdade(self):
		self.__idade = idade

	def fazerAniv(self):
		...


class Aluno(Pessoa):
	__matr = int
	__curso = str

	# def __init__(self, nome, idade, sexo):
	# 	super().__init__(self, nome, idade, sexo)

	def getMatr(self):
		return self.__matr

	def setMatr(self, matr):
		self.__matr = matr

	def getCurso(self):
		return self.__curso

	def setCurso(self, curso):
		self.__curso = curso

	def cancelarMatr(self):
		...


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


class Funcionario(Pessoa):
	__setor = str
	__trabalhando = bool

	# def __init__(self, nome, idade, sexo):
	# 	super().__init__(self, nome, idade, sexo)

	def getSetor(self):
		return self.__setor

	def setSetor(self, setor):
		self.__setor = setor

	def getTrabalhando(self):
		return self.__trabalhando

	def setTrabalhando(self, trabalhando):
		self.__trabalhando = trabalhando

	def mudarTrabalho(self):
		...




pes = Pessoa()
alu = Aluno()
pro = Professor()
fun = Funcionario()

pes.setNome('Clementina')
print(pes.getNome())

alu.setNome('Valeria')
print(alu.getNome())

pro.setNome('Kreuza')
print(pro.getNome())

fun.setNome('Paula')
print(fun.getNome())

alu.setCurso('Ciencia da computacao')
pro.setSalario(2345.67)
fun.setTrabalhando(True)
fun.setSetor('Estoque')

pro.receberAum(500)




