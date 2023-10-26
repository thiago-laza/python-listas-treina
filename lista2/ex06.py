"""6.Escreva um algoritmo que receba o valor da idade de uma pessoa e escreva sua classificação
segundo a seguinte tabela abaixo:
• maior de idade (Idade Superior ou igual a 21 Anos)
• menor de idade (Idade Inferior a 21);
• pessoa idosa (idade superior ou igual a 65 anos)."""

idade = int(input('Digite sua idade: '))

if idade < 21:
    print(f'Voce com {idade} anos e MENOR DE IDADE.')
elif idade >= 21 and idade < 65:
    print(f'Voce com {idade} anos e MAIOR DE IDADE.')
else:
    print(f'Voce com {idade} anos e IDOSO.')