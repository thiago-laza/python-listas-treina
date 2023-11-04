"""5. Uma pesquisa sobre algumas características físicas da população de uma determinada região
coletou os seguintes dados referentes a cada habitante para serem analisados:
• Sexo (“M” - Masculino, “F” - Feminino)
• Cor dos Olhos (“A”-Azul,”V”-Verde, “C’-Castanho)
• Idade em anos
Para cada habitante foi digitada uma linha com esses dados e a última linha, que não corresponde a
ninguém conterá o valor de idade igual a -1. Fazer um programa que determine e imprima:
a) A maior idade dos habitantes;
b) A porcentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e
que tenham olhos verdes;"""

maior_idade = 0

acrescentar_habitante = 's'

cont = 0
cont_fem = 0

while acrescentar_habitante == 's':
    cont += 1
    sexo = str(input('Sexo (m/f): '))
    cor = str(input('Cor dos olhos (a-azul/v-verde/c-castanho): '))
    idade = int(input('Idade: '))
    if idade > maior_idade:
        maior_idade = idade
    if sexo == 'f' and idade > 18 and idade <= 35 and cor == 'v':
        cont_fem += 1
    acrescentar_habitante = str(input('Deseja acrescentar outro habitante? (s/n): '))
    if acrescentar_habitante == 'n':
        break

print(f'A mairo idade dos habitantes foi de {maior_idade} anos.')
print(f'A porcentagem de mulheres com mais de 18 anos e ate 35 ano com olhos verdes e de {(cont_fem/cont)*100}%')
