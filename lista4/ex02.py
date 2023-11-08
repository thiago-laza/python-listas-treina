"""2.Elabore um programa que receba 5 placas de automóvel no formato
“LLLNLNN” onde: “L” são letras e “N” são números, calcule e exiba para cada
uma das placas recebidas a soma dos valores que estão nas posições “N”."""

placa = []
acu1 = 0
acu2 = 0
acu3 = 0

for i in range(1,3):
    inf = input('Digite a placa: ')
    placa.append(inf)
    primeiro = float(inf[3])
    acu1 += primeiro
    segundo = float(inf[5])
    acu2 += 2
    terceiro = float(inf[6])
    acu3 += terceiro





print(acu1+acu2+acu3)