"""7.Nome na vertical. Faça um programa que solicite o nome do usuário e
imprima-o na vertical.
o F
o U
o L
o A
o N
o O"""

nome = str(input('Digite seu nome: '))

for i in range(0,len(nome)):
    print(nome[i])