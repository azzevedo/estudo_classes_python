from pessoa import Pessoa

class PessoaJuridica(Pessoa):

	def __init__(self, cnpj, nome, idade):
		super().__init__(nome, idade)
		self.cnpj = cnpj