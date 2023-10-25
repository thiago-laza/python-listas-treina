"""11. Dado um número inteiro, positivo, menor do que 1000 obter a quantidade de
centenas, dezenas e unidades desse número.
Exemplo: Dado o nº 764, obter Centena = 7, Dezena = 6 e Unidade = 4"""

n = int(input('Digite um número inteiro menor que 1000: '))

c = n//100
d = (n - 100*c)//10
u = n - (c*100 + d*10)

print(f'O número {n} tem {c} centenas, {d} dezenas e {u} unidades.')

