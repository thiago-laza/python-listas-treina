"""
2. Faça um programa para ler dois valores nas variáveis A e B, e efetuar as trocas dos
valores de forma que a variável A passe a possuir o valor da variável B e a variável B
passe a possuir o valor da variável A. Apresentar os valores trocados.
"""

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))

print(f'O primeiro valor digitado foi {a} e o segundo valor digitado foi {b}')

c = a
d = b

c = b
d = a

a = c
b = d

print(f'Fazendo a troca dos valores, o primeiro valor passa a ser {a} e o segundo valor passa a ser {b}')

