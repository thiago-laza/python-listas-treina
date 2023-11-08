"""11. Escrever um programa que lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo
fechado entre 10 e 20 e quantos deles estão fora do intervalo, no final escreva estes resultados."""

cont = 0

for i in range(1,11):
    nun = float(input(f'Digite o {i}⁰ valor: '))
    if nun > 10 and nun < 20:
        cont += 1


print(f'Dos 10 numeros digitados {cont} estao no intervalo entre 10 e 20 e {10 - cont} estao fora do intervalo entre 10 e 20.')
    