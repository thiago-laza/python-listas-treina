"""4.A Cidade de São Paulo precisará acrescentar um algarismo 9 na frente de
cada um dos 3 números de celulares informados via teclado no formato
011NNNN-NNNN. Elabore um programa que receba os números originais e
para cada um escreva o número com a modificação sugerida, ou seja,
0119NNNN-NNNN."""

for i in range(1,4):
    tel = str(input(f'Digite o {i}⁰ numero: '))
    tel1 = tel[:3]
    tel2 = tel[3:]
    print(f'O numero {tel} ficara', tel1 +'9'+tel2)