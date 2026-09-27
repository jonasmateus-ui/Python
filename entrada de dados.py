nome1: str; nome2: str
idade: int
salario1: float; salario2: float
sexo: str

nome1 = input("nome da primeira pessoa: ")
salario1 = float(input("salario da primeira pessoa: "))

nome2 = input("nome da segunda pessoa: ")
salario2 = float(input("salario da segunda pessoa: "))

idade =  int(input("digite uma idade: "))
sexo = input("digite um sexo: F ou M: ")

print (f"nome1 {nome1}")
print (f"Salario1: {salario1:.2f}")

print (f"nome2 {nome2}")
print (f"Salario2: {salario2:.2f}")
print(f"idade: {idade}")
print(f"sexo: {sexo}")
