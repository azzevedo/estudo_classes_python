class Veiculo():
    def __init__(self, possuiMotor, rodas):
        self.rodas = rodas
        self.possuiMotor = possuiMotor
        self.ligado = False
        self.andando = False

    def ligar(self):
        if self.andando or self.ligado:
            print("O veículo já está ligado")
        else:
            print("Iniciando o motor")
            self.ligado = True

    def desligar(self):
        if self.andando:
            self.parar()
            print("Desligando o motor")
            self.ligado = False
        elif self.ligado:
            print("Desligando o motor")
            self.ligado = False
        else:
            print("O veículo já está desligado")

    def andar(self):
        if self.andando:
            print("O veículo já está andando")
        elif self.ligado:
            self.andando = True
            print("Andando")
        else:
            self.ligar()
            self.andando = True
            print("Andando")

    def parar(self):
        if self.andando:
            print("Parando veículo")
            self.andando = False
        else:
            print("O veículo já está parado")







