print('Bem vindo ao jom NIM! escolha: ')

def inicio():
    print('1 - PARA JOGAR PARTIDA ISOLADA \n2 - PARA JOGAR CAMPEONATO\n')

    x = int(input())

    if (x != 1) and (x !=2):
        if x == 1:
            print('Voce escolheu uma partida isolada!\n')
            return 1
        elif x == 2:
            print('Voce escolheu um campeonato!\n')
            return 2
        else:
            print('Digite uma opção valida\n')
            x = 0
            return inicio()


def computador_escolhe_jogada(n, m):
    jogada = n % (m + 1)
    if jogada == 0:
        jogada = m
    return jogada

def usuario_escolhe_jogada(n, m):
    jogada = jogado = int(input('Quantas peças voce vai tirar? '))
    while jogada > m or jogada > n or jogada <1 :
        print('Limite maximo de peças igual a %d' %m)
        jogada = int(input('Quantas peças voce vai tirar? '))
    return  jogada

def partida(n, m):
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        jogador = 'usuario'
    else:
        print("\nComputador começa!\n")
        jogador = "computador"
    while n > 0:
        if jogador == 'usuario':
            jogada = usuario_escolhe_jogada(n, m)
            n = n - jogada
            print('Voce tirou', jogada, 'peças.')
            jogada = 'computador'
        else:
            jogada = computador_escolhe_jogada(n, m)
            n = n - jogada
            print("O computador tirou", jogada, "peças.")
            jogador = "usuario"
        print("Agora restam", n, "peças no tabuleiro.\n")
        if jogador == "usuario":
            print("O computador ganhou!")
        else:
            print("Você ganhou!")

def partida_Isolada():
    print("Voce escolheu uma partida isolada!")
    n = int(input("Quantas peças?"))
    m = int(input("Limite de peças por jogada?"))
    print(partida(n, m))


def campeonato():
    print("Voce escolheu um campeonato!")

    for x in range(1, 4):
        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças por jogada?"))
        print("**** Rodada %d ****" % x)
        print(partida(n, m))


if inicio() == 1:
    print(partida_Isolada())
else:
    print(campeonato())
