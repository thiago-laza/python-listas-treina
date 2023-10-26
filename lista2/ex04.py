"""4.Escreva um algoritmo que receba um valor numérico de 3(três) dígitos e exiba a soma dos
algarismos que compõe este número. Exemplo: 145 -> 1+4+5 = 10"""

n = int(input('Digite um numero de 3 digitos? '))

c = n // 100
d = (n - 100*c) // 10
u = n - (c*100 + d*10)

soma = c+d+u 

print(f'A soma dos valore dos algarismos do numero {n} e igual a {soma}')

