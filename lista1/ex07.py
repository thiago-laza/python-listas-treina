"""7. Faça um programa que receba o preço de custo de um produto e mostre o valor de
venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um
percentual informado pelo usuário."""

c = float(input("Informe o valor de custo do produto: "))
p = float(input("Informe o percentual de acréscimo: "))

v = c*(1+p/100)

print(f'O custo no valor de R$ {c} com um acréscimo de {p}% terá um valor de venda de R$ {round(v,2)}')