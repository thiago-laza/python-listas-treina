"""4. Faça um programa que leia o nome e a idade de 15 pessoas e apresente:
a. Maior idade
b. Nome da pessoa mais nova
c. Média das idades"""


maidade = 0
meidade = 10**100
nomemaior = ''
nomemenor = ''
somaidade = 0
cont = 0

for i in range(1,16):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    somaidade += idade
    cont += 1

    if idade > maidade:
        maidade = idade
        nomemaior = nome
    if idade < meidade:
        meidade = idade
        nomemenor = nome

media = somaidade /  cont

print(f'A media das idades das {cont} pessoas e de {media} anos')
print(f'A pessoa mais velha e {nomemaior} que tem {maidade} anos')
print(f'A pessoa mais nova e {nomemenor} que tem {meidade} anos')





