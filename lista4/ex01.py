"""1.Elabore um programa que receba 5 frases e no final exiba o total de letras
“A” existentes em todas as frases digitadas."""

cont = 0

for i in range(1,6):
    frase = input(f'Digete a {i}⁰ frase: ')
    for letra in frase:
        if letra == 'a':
            cont += 1





print(cont)