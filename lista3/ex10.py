"""10. Faça um programa que fique lendo valores até encontrar o valor zero, com cada valor lido faça a
soma dos 10 valores subsequentes e mostre a soma e a média desses valores."""

soma = 0

num = int(input('Digite um numero: '))
for i in range(num,num+10):
    soma += i

media = soma/10

print(f'A soma dos valores subsequentes e {soma} e a media e {media}')
