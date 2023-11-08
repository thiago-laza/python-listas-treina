"""4.A Cidade de São Paulo precisará acrescentar um algarismo 9 na frente de
cada um dos 3 números de celulares informados via teclado no formato
011NNNN-NNNN. Elabore um programa que receba os números originais e
para cada um escreva o número com a modificação sugerida, ou seja,
0119NNNN-NNNN."""

novo = []
new = []

for i in range(1,4):
    telefone = input(f'Informe o numero do {i}⁰ telefone: ')
    novo.append(telefone)
    new.insert(0,'9')

print(new)