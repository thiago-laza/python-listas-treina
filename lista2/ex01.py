"""1.Escreva um algoritmo que solicita ao usuário para digitar um número inteiro positivo, e mostre-
o por extenso. Este número deverá variar entre 1 e 10. Se o usuário introduzir um número que
não pertença a este intervalo, exiba a mensagem: “número inválido”. Exemplo: 10 ➔ Dez; 7
➔ Sete ; 2 ➔ Dois"""

n = int(input('Digite um numero de 1 ate 10: '))

if n == 1:
    print('UM')
elif n == 2:
    print('DOIS')
elif n == 3:
    print('TRES')
elif n == 4:
    print('QUATRO')
elif n == 5:
    print('CINCO')
elif n == 6:
    print('SEIS')
elif n == 7:
    print('SETE')
elif n == 8:
    print('OITO')
elif n == 9:
    print('NOVE')
elif n == 10:
    print('DEZ')
else:
    print('Valor invalido')