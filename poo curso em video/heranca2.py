#!/usr/bin/python3

# classe abstrata
class Pessoa:
	# Também tem os setters e getters
	__nome = str
	__idade = int
	__sexo = str

	# Metodo final (não pode ser sobrescrito)
	def fazer_aniversario():
		...



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

	def pagar_mensalidade(self):
		...



class Bolsista(Aluno):
	__bolsa = int

	def renovar_bolsa(self):
		...

	# Sobreposição
	def pagar_mensalidade(self):
		...



class Tecnico(Aluno):
	
	__registro_profissional = int
	
	def praticar(self):
		...



