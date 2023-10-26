"""8.Construa um algoritmo para determinar se o indivíduo está
com um peso favorável ou não. Essa situação é
determinada através do IMC ( Índice de Massa
Corpórea), que é definida como sendo a relação entre o
peso (PESO) e o quadrado da Altura (ALTURA) do
indivíduo. A situação do peso é determinada pela fórmula:"""

p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))

imc = p / (a**2)

if imc < 20:
    print('Voce esta abaixo do peso')
elif imc >= 20 and imc <= 45:
    print('Voce')