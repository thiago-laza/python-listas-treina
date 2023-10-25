"""4. Elaborar um programa que efetue a apresentação do valor da conversão em real (R$)
de um valor lido em dólar (US$). O programa deverá solicitar o valor da cotação do
dólar e a quantidade de dólares disponíveis com o usuário."""

print('Convertendo de dólar para real')

d = float(input('Informe o valor em Dólar: '))
c = float(input('Informe a cotação do Dólar em comparação com o Real: '))

r = c*d

print(f'U$ {d} vale R$ {r}')