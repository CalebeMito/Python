def preencherInventario(lista):
    resp= 'S'
    while resp == 'S':
        equipamento = (input('EQUIPAMENTO : '),
                       float(input('VALOR : ')),
                       int(input('NUMERO SERIAL : ')),
                       input('DEPARTAMENTO : '))
        inventario.append(equipamento)
        resposta = input('DIGITE \'S\'PARA CONTINUAR ').upper()

def exibirInventario(lista):
    for elemento in inventario:
        print('nome..............:', elemento[0])
        print('valor.............:', elemento[1])
        print('serial..........:', elemento[2])
        print('Departamento..........:', elemento[3])

def localizarPorNome(lista):
    busca = input('\nDIGITE O NOME DO EQUIPAMENTO QUE VOCE QUER PESQUISAR : ')
    for elemento in inventario:
        if busca == elemento[0]:
            print('VALOR :', elemento[1])
            print('NUMERO DE SERIE :', elemento[2])

def depreciarPorNome(lista):
    depreciacao = input('\nDIGITE O NOME DO EQUIPAMENTO QUE VAI SER DEPRECIADO :')

    for elemento in inventario:
        if depreciacao == elemento[0]:
            print('VALOR ANTIGO', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('NOVO VALOR :', elemento[1])

def  excluirPorSerial(lista):
    serial = int(input('\nDIGITE O NUMERO DE SERIE QUE SERA EXCLUIDO :'))
    for elemento in inventario:
        valores.append(elemento[1])
    if elemento[2] == serial:
        inventario.remove(elemento)
    return 'itens excluidos .'

def resumirValores(lista):
    valores = []

    for elemento in inventario:
        valores.append(inventario)
    if len(valores9) > 0:
        print('O EQUIPAMENTO MAIS CARO CUSTA :', max(valores))
        print('O EQUIPAMENTO MAIS BARATO CUSTA :', min(valores))
        print('O TOTAL DE EQUIPAMENTOS E DE :', sum(valores))


minhaLista=[]
print('PREENCHENDO...')
preencherInventario(minhaLista)
print('EXIBINDO...')
exibirInventario(minhaLista)

print('PESQUISANDO...')
localizarPorNome(minhaLista)
print('ALTERANDO...')
depreciarPorNome(minhaLista)

print('EXCLUINDO...')
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print('RESUMINDO...')
resumirValores(minhaLista)

