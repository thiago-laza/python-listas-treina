"""7. Um palíndromo é uma sequência de caracteres que sendo lida da esquerda para a direita ou da
direita para a esquerda tem o mesmo valor. Por exemplo, cada um dos seguintes inteiros de 5
dígitos é um palíndromo: 12321, 55555, 45554 e 11611. Escreva um aplicativo que leia uma
sequência de números de 5 dígitos e determine se ele é ou não um palíndromo."""

n = int(input('Escreva um numero de 5 algarismos para verificar se ele e ou nao um palindromo: '))

p = n // 10000
u = n % 10

s = (n - p*10000) // 1000
pn = (n % 100) // 10

if p == u and s == pn:
    print(f'O numero {n} e um palindromo')
else:
    print(f'O numero {n} nao e um palindromo')

