nome: str
salario: float
idade : int
altura: float
peso: float
sexo: str

nome = 'Maria silva'
salario = 4560.9
idade = 32
altura = 168.5
peso = 70
sexo = 'F'

print (f"A funcionária {nome}, sexo {sexo}, ganha {salario:.2f}, e tem {idade} anos")

print ("a funcionária {:s}, sexo {:s}, ganha {:f}, tem {:d} anos ".format(nome, sexo, salario, idade))