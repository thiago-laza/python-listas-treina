"""6. A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem
juros. Faça um programa que receba um valor de uma compra e mostre o valor das
prestações."""

v = float(input('Informe o valor da compra: '))

p = v/5

print(f'A compra no valor de R$ {v} fica em 5 x de R$ {p}')