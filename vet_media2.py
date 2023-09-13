N = int(input("Quantos precos voce vai digitar? "))
soma = 0
vet = []

for i in range(0, N):
aux = int(input('digite os precos :'))
vet.append(aux)
soma = soma + vet[i]

md=(soma / N)

print()
print("NUMEROS DIGITADOS:")

for i in range(0, N):
print(f'{vet[i]}')

print('A soma e de :', soma)
print('a media dos precos e de :',md)

print('NUMEROS MAIORES QUE A MEDIA :')

for i in range(0, N):
if (vet[i] > md):
print(f"{vet[i]}")
