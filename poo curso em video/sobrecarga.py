from copyreg import dispatch_table
from tabnanny import verbose
from multipledispatch import dispatch

'''
@dispatch(int, int, int)
def soma(a, b, c):
	return a + b + c

@dispatch(float, int)
def soma(a, b):
	return a + b


print(soma(1.0, 2))
print(soma(3, 5, 3))
'''

class Animal:
	#protegido
	peso = float
	idade = int
	membros = int

	#metodo 'abstrato'
	def emitir_som(self):
		...


class Mamifero(Animal):
	# protegido
	cor_pelo = str

	def emitir_som(self):
		print('Som de mamifero')


class Lobo(Mamifero):

	def emitir_som(self):
		print('Auuuuuuuuuuuuuuuu!')


class Cachorro(Lobo):

	def emitir_som(self):
		print('Au! Au! Au!')

	@dispatch(str)
	def reagir(self, frase):
		if frase == 'toma comida' or frase == 'ola':
			print('Abanar e latir')
		else:
			print('Rosnar')

	@dispatch(int, int)
	def reagir(self, hora, min):
		if hora < 12:
			print('Abanar')
		elif hora < 18:
			print('Abanar e Latir')
		else:
			print('Ignorar')

	@dispatch(bool)
	def reagir(self, dono):
		if dono:
			print('Abanar')
		else:
			print('Rosnar e Latir')

	@dispatch(int, float)
	def reagir(self, idade, peso):
		if idade < 5:
			if peso < 10:
				print('Abanar')
			else:
				print('Latir')
		else:
			if peso < 10:
				print('Rosnar')
			else:
				print('Ignorar')



c = Cachorro()
c.reagir('ola')
c.reagir('vai apanhar')

c.reagir(11, 45)
c.reagir(21, 00)

c.reagir(True)
c.reagir(False)

c.reagir(2, 12.5)
c.reagir(17, 4.5)



