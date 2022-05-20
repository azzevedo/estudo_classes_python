#!/usr/bin/python3

""" Polimorfismo """


# Classe abstrata
class Animal:

	_peso = float
	_idade = int
	_membros = int

	def set_peso(self, peso):
		self._peso = peso

	def set_idade(self, idade):
		self._idade = idade

	def set_membros(self, membros):
		self._membros = membros

	# Também tem os getters

	def locomover(self):
		...

	def alimentar(self):
		...

	def emitir_som(self):
		...


class Mamifero(Animal):
	__cor_pelo = str

	def get_cor_pelo(self):
		return self.__cor_pelo
	
	def set_cor_pelo(self, cor):
		self.__cor_pelo = cor

	def locomover(self):
		print('Correndo')

	def alimentar(sefl):
		print('Mamando na teta da tua mãe')

	def emitir_som(self):
		print('Som de mamífero')


class Reptil(Animal):
	__cor_escama = str

	def get_cor_escama(self):
		return self.__cor_escama

	def set_cor_escama(self, cor):
		self.__cor_escama = cor

	def locomover(self):
		print('Rastejando')

	def alimentar(self):
		print('Comendo vegetais')

	def emitir_som(self):
		print('Som de réptil')


class Peixe(Animal):
	__cor_escama = str

	def get_cor_escama(self):
		return self.__cor_escama

	def set_cor_escama(self, cor):
		self.__cor_escama = cor

	def soltar_bolha(self):
		print('Soltar bolha')

	def locomover(self):
		print('Nadando')

	def alimentar(self):
		print('Comendo plancton')

	def emitir_som(self):
		print('Glub glub')


class Ave(Animal):
	__cor_pena = str

	def get_cor_pena(self):
		return self.__cor_pena

	def set_cor_pena(self, cor):
		self.__cor_pena = cor

	def fazer_ninho(self):
		print('Construiu um ninho')

	def locomover(self):
		print('Voando')

	def alimentar(self):
		print('Comendo frutas')

	def emitir_som(self):
		print('Som de ave')


class Canguru(Mamifero):
	
	def usar_bolsa(self):
		print('Filhote na bolsa')

	def locomover(self):
		print('Saltando')


class Cachorro(Mamifero):
	
	def enterrar_osso(self):
		print('Enterrando osso')

	def abanar_rabo(self):
		print('Abanando rabo')

	def emitir_som(self):
		print('AU AU AU')



class Cobra(Reptil):
	...


class Tartaruga(Reptil):

	def locomover(self):
		print('Andando a 1 metro por hora')


class Goldfish(Peixe):
	...


class Arara(Ave):
	...






m = Mamifero()
r = Reptil()
p = Peixe()
a = Ave()

m.set_peso(85.3)
m.set_idade(2)
m.set_membros(4)
m.locomover()
m.alimentar()
m.emitir_som()


p.set_peso(0.35)
p.set_idade(1)
p.set_membros(0)
p.locomover()
p.alimentar()
p.emitir_som()
p.soltar_bolha()


a.set_peso(0.89)
a.set_idade(2)
a.set_membros(2)
a.locomover()
a.alimentar()
a.emitir_som()
a.fazer_ninho()


m1 = Mamifero()
c = Canguru()
k9 = Cachorro()

m1.set_peso(55.70)
m1.set_idade(27)
m1.set_membros(4)
m1.locomover()
m1.alimentar()
m1.emitir_som()

c.set_peso(65.23)
c.set_idade(3)
c.set_membros(4)
c.locomover()
c.alimentar()
c.emitir_som()
c.usar_bolsa()

k9.set_peso(3.62)
k9.set_idade(5)
k9.set_membros(4)
k9.locomover()
k9.alimentar()
k9.emitir_som()
k9.abanar_rabo()

################################
print('Exemplos da aula pratica')

mamifero = Mamifero()
reptil = Reptil()
peixe = Peixe()
ave = Ave()
canguru = Canguru()
cachorro = Cachorro()
cobra = Cobra()
tartaruga = Tartaruga()
goldfish = Goldfish()
arara = Arara()

mamifero.set_peso(35.3)
mamifero.set_cor_pelo('Preto')
mamifero.alimentar()
mamifero.locomover()
mamifero.emitir_som()

ave.locomover()
peixe.locomover()
reptil.locomover()
canguru.usar_bolsa()
canguru.locomover()
cachorro.locomover()
cachorro.emitir_som()

