def multiplicacao(km, km_percorrido, valor_combustivel, total):
    calculo = (km_percorrido / km) * valor_combustivel
    calculo = calculo + total
    print('Voce ira gastar {:.2f}'.format(calculo))


print('Qual combustivel voce utiliza?')
tipo_combustivel = int(input('Para alcool digite - 1, gasolina digite - 2, disel digite - 3 :  '))

km_percorrido = float(input('Digite a kilometragem que ira percorre: '))


print('possui pedagio no percurso ? ')
pergunta = str(input("Se tiver digite S, caso contrario digite N: "))
pergunta = pergunta.upper()
total = float
total = 0

if (pergunta == 'S'):
    pedagios = int(input('Quantos pedagios tem no percurso ? '))
    for pedagio in range (1,pedagios + 1):
        valor_pedagio = float(input('Qual o valor do {}° pedagio '.format(pedagio)))
        total = total + valor_pedagio
else:
    pass

if (tipo_combustivel == 1):
    km = float(input('Digite a quantidade de kilometros a cada 1 Litro de Alcool: '))
    valor_combustivel = float(input('Digite o valor do Litro do Alcool: '))
    multiplicacao(km, km_percorrido, valor_combustivel, total)

if (tipo_combustivel == 2):
    km = float(input('Digite a quantidade de kilometros a cada 1 Litro da Gasolina: '))
    valor_combustivel = float(input('Digite o valor do Litro do Gasolina: '))
    calculo = (km_percorrido / km) * valor_combustivel
    multiplicacao(km, km_percorrido, valor_combustivel, total)

if (tipo_combustivel == 3):
    km = float(input('Digite a quantidade de kilometros a cada 1 Litro de Disel: '))
    valor_combustivel = float(input('Digite o valor do Litro do Disel: '))
    calculo = (km_percorrido / km) * valor_combustivel
    multiplicacao(km, km_percorrido, valor_combustivel, total)

if (tipo_combustivel > 3):
    print('Numero invalido, por favor digite novamente')
