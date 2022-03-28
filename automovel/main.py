
# Online Python - IDE, Editor, Compiler, Interpreter
from carro import Carro
from bicicleta import Bicicleta

bike = Bicicleta(2)
print("Possui motor:", bike.possuiMotor)
print("Possui guidão:", bike.possuiGuidao)
print("Está ligado:", bike.ligado)
print("Está andando:", bike.andando)


bike.ligar()
bike.andar()
bike.parar()
bike.desligar()

print("Está ligado:", bike.ligado)
print("Está andando:", bike.andando)

print("Está ligado:", bike.ligado)
print("Está andando:", bike.andando)

bike.empinar()
print("============== FIM DA BICICLETA ==============================")
print("\n\n===========================  CARRO ==================================")

carro = Carro(4)
print(carro.rodas)
print("Possui motor:", carro.possuiMotor)
print("Está ligado:", carro.ligado)
print("Está andando:", carro.andando)

carro.desligar()
carro.parar()
carro.andar()
carro.ligar()
carro.andar()
carro.parar()
carro.ligar()
carro.desligar()





