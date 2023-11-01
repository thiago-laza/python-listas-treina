"""8.Construa um algoritmo para determinar se o indivíduo está
com um peso favorável ou não. Essa situação é
determinada através do IMC ( Índice de Massa
Corpórea), que é definida como sendo a relação entre o
peso (PESO) e o quadrado da Altura (ALTURA) do
indivíduo. A situação do peso é determinada pela fórmula:"""

p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))

imc = round(p / (a**2),1)

if imc < 20:
    print(f'Seu IMC = {imc} e voce esta abaixo do peso')
elif imc >= 20 and imc <= 25:
    print(f'Seu IMC = {imc} e voce esta com peso normal')
elif imc > 25 and imc <= 30:
    print(f'Seu IMC = {imc} e voce esta com sobrepeso')
elif imc > 30 and imc <= 40:
    print(f'Seu IMC = {imc} e voce esta obeso(a)')
else:
    print(f'Seu IMC = {imc}voce esta com obesidade morbida')