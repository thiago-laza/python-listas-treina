"""5. Faça um programa que receba um valor que foi depositado e exiba o valor com
rendimento após um mês. Considere fixo o juro da poupança em 0,50% a. m."""

v = float(input('Informe o valor depositado: '))


r = v*(1+0.5/100)

print(f'O valor de R${v} teve rendimento de {round(r-v,2)} e pasou a valer {round(r,2)}')