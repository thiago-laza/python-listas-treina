"""9.Faça um programa que leia um número indeterminado de números, o programa encerra quando for
digitado o número 99. O programa deve fornecer ao final o percentual de números pares e ímpares
digitados."""

cont = 0
cont_par = 0
cont_impar = 0


while True:
    num = float(input('Digite um numero: '))
    if num == 99:
        break
    cont += 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'Dos {cont} numeros digitados, {round((cont_par/cont)*100,1)}% sao pares e {round((cont_impar/cont)*100,1)}% sao impares.')