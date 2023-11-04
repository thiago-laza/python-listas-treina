"""7.Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contando seu
número de identificação e seu peso. Fazer um programa que escreva o número e peso do boi mais
gordo e do boi mais magro."""

menor_peso = 10**100
maior_peso = 0
num_menor_peso = ''
num_maior_peso = ''

for i in range(1,91):
    num = int(input(f'Informe a numeracao do {i}⁰ boi: '))
    peso = float(input(f'Informe o peso do {i}⁰ boi: '))
    if peso < menor_peso:
        menor_peso = peso
        num_menor_peso = num
    if peso > maior_peso:
        maior_peso = peso
        num_maior_peso = num

print(f'O menor peso foi o boi de numeracao {num_menor_peso} pesando {menor_peso}kg')
print(f'O maior peso foi o boi de numeracao {num_maior_peso} pesando {maior_peso}kg')