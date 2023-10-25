
"""
1. Faça um programa que receba dois números e ao final mostre a soma, subtração,
multiplicação e a divisão dos números lidos.
"""

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = n1+n2
sub = n1-n2
mul = n1*n2
div = n1/n2

print(f'A soma entre {n1} e {n2} é igual a {soma}')
print(f'A subtração entre {n1} e {n2} é igual a {sub}')
print(f'A multiplicação entre {n1} e {n2} é igual a {mul}')
print(f'A divisão entre {n1} e {n2} é igual a {div}')
