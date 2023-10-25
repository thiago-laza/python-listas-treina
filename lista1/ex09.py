"""9. Faça um programa que leia a idade de uma pessoa expressa em anos, meses e dias
e mostre-a expressa apenas em dias, suponha todos os meses com 30 dias."""

print('Informe sua idade:')
a = int(input('Anos: '))
m = int(input('Meses: '))
d = int(input('Dias: '))

da = a*360
dm = m*30

idade = da+dm+d

print(f'Uma pessoa que tem {a} anos, {m} meses e {d} dias tem {idade} dias de vida.')