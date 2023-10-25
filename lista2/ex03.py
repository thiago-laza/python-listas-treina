"""3.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso
contrário, ele será classificado como "Inocente"."""

print('Responta sim(s) ou nao(n)')

s = 0


p1 = str(input('Telefonou para vitima? '))
if p1 == 's':
    s+=1
p2 = str(input('Esteve no local do crime? '))
if p2 == 's':
    s+=1
p3 = str(input('Mora perto da vitma? '))
if p3 == 's':
    s+=1
p4 = str(input('Devia para a vitima? '))
if p4 == 's':
    s+=1
p5 = str(input('Ja trabalhou com a vitima? '))
if p5 == 's':
    s+=1



if s == 2:
    print('Suspeita')
elif s == 3 or s == 4:
    print('Cumplice')
elif s == 5:
    print('Assassino')
else:
    print('Inocente')

