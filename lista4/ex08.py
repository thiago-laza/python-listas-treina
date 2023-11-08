"""8. Nome na vertical em escada. Modifique o programa anterior de forma a
mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO"""

nome = str(input('Digite seu nome: '))

cont = 0

for i in range(0,len(nome)):
    print(nome[:i])