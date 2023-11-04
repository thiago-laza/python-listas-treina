"""10. Faça um programa que fique lendo valores até encontrar o valor zero, com cada valor lido faça a
soma dos 10 valores subsequentes e mostre a soma e a média desses valores."""

cont = 0
acu = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    else:
        acu += num
        cont += 1
        if cont == 10:
            