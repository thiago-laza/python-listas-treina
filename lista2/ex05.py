"""5.Escreva um algoritmo que receba um número e verifique se ele é múltiplo de 3 e de 7. Escreva
uma das mensagens: “é múltiplo de 3 e de 7” ou “não é múltiplo de 3 e 7”."""

n = int(input('Escreva um numero para verificar se ele e multiplo de 3 e 7: '))

if n%3 == 0 and n%7 == 0:
    print(f'O numero {n} e multiplo de 3 e 7')
else:
    print(f'O numero {n} nao e multiplo de 3 e 7')