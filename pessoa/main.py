from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

pf = PessoaFisica("123.134.134-42", "Fulano de Tal", 32)
pj = PessoaJuridica("42.323.425/8478-99", "Nome Fantasia", 3)

print("Nome:", pf.nome)
print("CPF:", pf.cpf)
print("Idade:", pf.idade)

print("Nome:", pj.nome)
print("CNPJ:", pj.cnpj)
print("Idade:", pj.idade)