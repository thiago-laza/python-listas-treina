"""8.Fazer um programa que: Leia um número indeterminado de linhas contendo cada uma a idade de
um indivíduo. A última linha que não entrará nos cálculos contém o valor da idade igual à zero.
Calcule e imprima a idade média deste grupo de indivíduos."""

continuar = 's'
cont = 1
acu = 0

while continuar == 's':
    idade = int(input(f'Digite a idade de {cont}⁰ pessoa: '))
    acu += idade
    cont += 1
    continuar = str(input('Deseja continuar?(s/n) '))
    if continuar == 'n':
        break

media = acu/(cont-1)

print(f'A media de idades das {cont-1} pessoas e igual a {media} anos.')