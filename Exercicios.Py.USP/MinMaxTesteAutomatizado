def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min 

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max       

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("valoe errado para array", temp)
        print("valor esperado :", valor_esperado, ". valor calculado :", valor_calculado)
 
def testa_minima():
    print("iniciando testes")
    teste_pontual([0], 0)

    teste_pontual([0, 0, 0, 0, 0, 0], 0) 
    
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0 )  
    
    teste_pontual([30, 27, 26, 25, 24, 23, 31, 29, 22], 22)  
    
    teste_pontual([-15, -13, -12, 0, 20, 30], -15)
    
    print("Finalizando os testes")
