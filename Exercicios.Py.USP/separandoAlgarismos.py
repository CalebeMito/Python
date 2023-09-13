numero = int(input("Digite um número inteiro: "))
i = 1
soma = 0
numeroconvertido = str(numero)
leitura = len(numeroconvertido)
while i <= leitura:
      ind_1 = numero % 10 
      soma = soma + ind_1
      numero = numero // 10
      i = i + 1

print(soma)
