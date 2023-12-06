from tkinter import Y


def funcaodeaprovados(x):
    if (x < 7):
        return 'reprovado'
    else :
        return 'aprovado'
    

def funcaomedia(n1, n2, n3) :
    media = (n1 + n2 + n3) / 3
    return media 
 
mediatotal = 0

for i in range (0,3):
    nota1 = int(input('digite a primeira nota :'))
    nota3 = int(input('digite a segunda nota :'))
    nota2 = int(input('digite a terceira nota :'))      

    y = funcaomedia(nota1,nota2,nota3)

    print('a media dos numeros e de :', y )
    print('o aluno foi : ----->', funcaodeaprovados(y))  
    mediatotal = mediatotal + y

print (mediatotal/ 3)            
