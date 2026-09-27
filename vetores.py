

n: int
n = int(input("Digite um numero: "))
vet: [float] = [0 for i in range (n)]

for i in range (n):
    vet[i] = float(input("Digite um numero: "))

print()
print("Numeros digitados:")
for i in range(0,n):
    print(f"{vet[i]:.1f}")