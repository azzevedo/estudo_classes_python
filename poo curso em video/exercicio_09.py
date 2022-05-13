#!/usr/bin/python3

class Pessoa():
	__nome = str
	__idade = int
	__sexo = str

	def __init__(self, nome, idade, sexo):
		self.__nome = nome
		self.__idade = idade
		self.__sexo = sexo

	def getNome(self):
		return self.__nome

	def setNome(self, nome):
		self.__nome = nome

	def getIdade(self):
		return self.__idade

	def setIdade(self, idade):
		self.__idade = idade

	def getSexo(self):
		return self.__sexo

	def setSexo(self, sexo):
		self.__sexo = sexo

	def fazerAniver(self):
		self.__idade += 1
		#self.setIdade(self.getIdade() + 1)
		print('Parabéns pra você nessa data querida!')



class IPublicacao:

	def abrir(self):
		raise NotImplementedError('Implementar')

	def fechar(self):
		raise NotImplementedError('Implementar')

	def folhear(self):
		raise NotImplementedError('Implementar')

	def avancarPag(self):
		raise NotImplementedError('Implementar')

	def voltarPag(self):
		raise NotImplementedError('Implementar')



class Livro(IPublicacao):

	__titulo = __autor = str
	__totPaginas = __pagAtual = int
	__aberto = bool
	__leitor = Pessoa

	def __init__(self, titulo, autor, totPaginas, leitor):
		self.__titulo = titulo
		self.__autor = autor
		self.__totPaginas = totPaginas
		self.__leitor = leitor
		self.__pagAtual = 0
		self.__aberto = False

	def detalhes(self):
		return f'Livro: {self.__titulo}\n' \
				f'Autor: {self.__autor}\n' \
				f'Total de páginas: {self.__totPaginas}\n' \
				f'Página atual: {self.__pagAtual}\n' \
				f'Aberto: {self.__aberto}\n' \
				f'Leitor: {self.__leitor.getNome()}\n' \
				f'Idade: {self.__leitor.getIdade()}\n' \
				f'Sexo: {self.__leitor.getSexo()}'

	def abrir(self):
		self.__aberto = True

	def fechar(self):
		self.__aberto = False

	def folhear(self, p):
		if p > self.__totPaginas:
			self.__pagAtual = self.__totPaginas
		else:
			self.__pagAtual = p

	def avancarPag(self):
		self.__pagAtual += 1

	def voltarPag(self):
		self.__pagAtual -= 1

	def setTitulo(self, titulo):
		self.__titulo = titulo
	
	def getTitulo(self):
		return self.__titulo

	def setAutor(self, autor):
		self.__autor = autor

	def getAutor(self):
		return self.__autor

	def setTotPaginas(self, tot):
		self.__totPaginas = tot

	def getTotPaginas(self):
		return self.__totPaginas

	def setPagAtual(self, pagAtual):
		self.__pagAtual = pagAtual

	def getPagAtual(self):
		return self.__pagAtual

	def setAberto(self, aberto):
		self.__aberto = aberto

	def getAberto(self):
		return self.__aberto

	def setLeitor(self, leitor):
		self.__leitor = leitor

	def getLeitor(self):
		return self.__leitor



p = []
livros = []

p.append(Pessoa('Joana', 32, 'F'))
p.append(Pessoa('Adriana', 39, 'F'))
livros.append(Livro('A revolta dos dandis', 'Humberto', 328, p[0]))
livros.append(Livro('Admiravel mundo novo', 'Aldous Huxley', 652, p[0]))
livros.append(Livro('A volta dos que nao foram', 'Anderson', 420, p[1]))


livros[0].abrir()
livros[0].folhear(30)
print(livros[0].detalhes())

livros[0].voltarPag()
print(livros[0].detalhes())

print(livros[2].detalhes())

