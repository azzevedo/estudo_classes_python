#!/usr/bin/python3
from multipledispatch import dispatch
"""
Exercício 14a, 15a
"""


class IAcoesVideo:
	"""
	Interface
	"""
	def play(self):
		...

	def pause(self):
		...

	def like(self):
		...


class Video(IAcoesVideo):
	"""
	Isso é python, então atributos privados deveriam começar com __nome_atributo
	Mas aqui todo mundo é adulto
	"""

	def __init__(self, titulo) -> None:
		self.titulo = titulo
		self.avaliacao = 1
		self.views = 0
		self.curtidas = 0
		self.reproduzindo = False

	def get_titulo(self):
		return self.titulo

	def set_titulo(self, titulo):
		self.titulo = titulo

	def get_avaliacao(self):
		return self.avaliacao

	def set_avaliacao(self, avaliacao):
		nova_av = (self.avaliacao + avaliacao) / self.views
		self.avaliacao = nova_av

	def get_views(self):
		return self.views

	def set_views(self, view):
		self.views += view

	def get_curtidas(self):
		return self.curtidas

	def set_curtidas(self, curtidas):
		self.curtidas = curtidas

	def get_reproduzindo(self):
		return self.reproduzindo

	def set_reproduzindo(self, rep):
		self.reproduzindo = rep

	def play(self):
		self.reproduzindo = True

	def pause(self):
		self.reproduzindo = False

	def like(self):
		self.curtidas += 1

	def __str__(self) -> str:
		return f'Video: {self.titulo}\n' \
				f'Avaliação: {self.avaliacao}\n' \
				f'Views: {self.views}\n' \
				f'Curtidas: {self.curtidas}\n' \
				f'Reproduzindo: {self.reproduzindo}'



class Pessoa:
	"""
	Classe 'abstrata'

	atributos protegidos
	em python, 1 underline
	_atributo_protegido
	"""

	def __init__(self, nome, idade, sexo):
		self.nome = nome
		self.idade = idade
		self.sexo = sexo
		self.experiencia = 0

	def get_nome(self):
		return self.nome

	def set_nome(self, nome):
		self.nome = nome

	def get_idade(self):
		return self.idade

	def set_idade(self, idade):
		self.idade = idade

	def get_sexo(self):
		return self.sexo

	def set_sexo(self, sexo):
		self.sexo = sexo

	def get_experiencia(self):
		return self.experiencia

	def set_experiencia(self, exp):
		self.experiencia = exp

	def ganhar_exp(self):
		...

	def __str__(self) -> str:
		return f'Nome: {self.nome}\n' \
				f'Idade: {self.idade}\n' \
				f'Sexo: {self.sexo}\n' \
				f'Experiência: {self.experiencia}'



class Gafanhoto(Pessoa):

	def __init__(self, nome, idade, sexo, login):
		super().__init__(nome, idade, sexo)
		self.login = login
		self.tot_video_assistido = 0

	def get_login(self):
		return self.login

	def set_login(self, login):
		self.login = login

	def get_tot_video_assistido(self):
		return self.tot_video_assistido

	def set_tot_video_assistido(self, tot):
		self.tot_video_assistido += tot

	def viu_mais_um(self):
		...

	def __str__(self) -> str:
		return super().__str__() + f'\nLogin: {self.login}\nVideos assistidos: {self.tot_video_assistido}'


class Visualizacao():

	def __init__(self, espectador, filme) -> None:
		self.espectador = espectador
		self.filme = filme
		self.espectador.set_tot_video_assistido(1)
		self.filme.set_views(1)

	def get_espectador(self):
		return self.espectador

	def set_espectador(self, espec):
		self.espectador = espec

	def get_filme(self):
		return self.filme

	def set_filme(self, filme):
		self.filme = filme

	@dispatch()
	def avaliar(self):
		self.filme.set_avaliacao(5)

	@dispatch(int)
	def avaliar(self, nota):
		self.filme.set_avaliacao(nota)

	@dispatch(float)
	def avaliar(self, porc):
		tot = 0
		if porc <= 20:
			tot = 3
		elif porc <= 50:
			tot = 5
		elif porc <= 90:
			tot = 8
		else:
			tot = 10
		self.filme.set_avaliacao(tot)

	def __str__(self) -> str:
		return f'Visualização{{espectador={self.espectador}, filme={self.filme}}}'
		'''
		return f'Espectador: {self.espectador.get_nome()}\n' \
				f'Filme: {self.filme.get_titulo()}'
		'''




videos = []
videos.append(Video('Aula 1 de POO'))
videos.append(Video('Aprenda POO em 5 minutos'))
videos.append(Video('Porque POO é importante'))


gafanhotos = []
gafanhotos.append(Gafanhoto('Rafaela', 20, 'F', 'rafix'))
gafanhotos.append(Gafanhoto('Jubileu', 35, 'M', 'juba'))


visu = []
visu.append(Visualizacao(gafanhotos[1], videos[2]))
visu[0].avaliar()
print(visu[0])

visu.append(Visualizacao(gafanhotos[1], videos[1]))
visu[1].avaliar(85.0)
print(visu[1])




"""
for v in videos:
	print('================')
	print(v)


for g in gafanhotos:
	print('=================')
	print(g)
"""


