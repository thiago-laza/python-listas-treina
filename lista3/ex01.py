"""1. Faça um programa que leia 20 idades e calcule a média aritmética delas;"""

cont = 0
acu = 0

while cont < 3:
    nota = float(input(f'Digite a {cont}⁰ nota: '))
    acu += nota
    cont += 1
media = acu / cont

print(f'A media das {cont} notas foi: {media}')