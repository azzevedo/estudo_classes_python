class Animal():
	def emitirSom(self):
		raise NotImplementedError("Não foi implementado")

class Cachorro(Animal):
	def emitirSom(self):
		print("Au au au")

class Gato(Animal):
	def emitirSom(self):
		print("Miau miau")

class Girafa(Animal):
	def comer(self):
		print("Comida gostosa")


def fazerBarulho(animal):
	animal.emitirSom()

dog = Cachorro()
cat = Gato()
giraffe = Girafa()

fazerBarulho(dog)
fazerBarulho(cat)
fazerBarulho(giraffe)