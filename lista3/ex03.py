"""3. Faça um programa que leia 20 números inteiros e apresente:
a. Média dos ímpares
b. Maior número par
c. Diferença do maior menos o menor número"""

par = 0
impar = 0

spar = 0
simpar = 0

mpar = 0
mepar = 10**100
mimpar = 0
meimpar = 10**100

for i in range(1,21):
    n = float(input(f'Digite o {i}⁰ numero: '))
    if n % 2 == 0:
        par += 1
        if n > mpar:
            mpar = n
        if n < mepar:
            mepar = n      
    else:
        simpar += n
        impar += 1
        if n > mimpar:
            mimpar = n
        if n < meimpar:
            meimpar = n




medimpar = simpar/impar

print(f'A media dos valores impares e: {medimpar}')
print(f'O maior par e {mpar}')
print(f'O menor par e {mepar}')
print(f'O maior impar e {mimpar}')
print(f'O menor impar e {meimpar}')
