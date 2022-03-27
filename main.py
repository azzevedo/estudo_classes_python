
# Online Python - IDE, Editor, Compiler, Interpreter
from carro import Carro
from bicicleta import Bicicleta

bike = Bicicleta(2)
print(bike.possuiMotor)
print(bike.possuiGuidao)
print(bike.ligado)
print(bike.andando)

bike.ligarDesligar()
bike.ligarDesligar()

bike.andarParar()
print(bike.ligado)
print(bike.andando)

bike.andarParar()
print(bike.ligado)
print(bike.andando)
bike.empinar()
print("============== FIM DA BICICLETA ==============================")
print("\n\n===========================  CARRO ==================================")

carro = Carro(4)
print(carro.rodas)
print(carro.possuiMotor)
print(carro.ligado)
print(carro.andando)






