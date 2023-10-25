"""8. Escrever um programa que leia o nome de um vendedor, o seu salário fixo e o total de
vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha
15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e
salário no final do mês."""

nome = str(input('Nome: '))
sal = float(input('Salário: '))
ven = float(input('Vendas: '))

com = ven*0.15

print(f'{nome} recebe um salário fixo de R$ {sal} com mais uma comissão de R$ {com} seu salário final é de R$ {sal+com}')