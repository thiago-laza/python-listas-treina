"""13. Tem-se um conjunto de dados contendo altura e sexo (“M” ou “F”) de 50 pessoas, fazer um
programa que calcule e escreva:
a) a maior e a menor altura do grupo
b) média de altura das mulheres
c) o número de homens"""

maior_altura = 0
menor_altura = 10**100
acu = 0
contm = 0
conth = 0

for i in range(1,51):
    alt = float(input(f'Digite a altura da {i}⁰ pessoa: '))
    if maior_altura < alt:
        maior_altura = alt

    if menor_altura > alt:
        menor_altura = alt
    sexo = input(f'Digite o sexo da {i}⁰ pessoa (m/f): ')
    if sexo == 'f':
        acu += alt
        contm += 1
    else:
        conth += 1

print(f'A menor altura foi de {menor_altura} m e a maior altura foi de {maior_altura} m.')
print(f'A media das alturas das {contm} mulheres foi de {acu/contm} m.')
print(f'Foram registrados {conth} homens.')

