"""10. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados, primeiro os impostos sobre o
custo de fábrica, e depois a percentagem do distribuidor sobre o resultado). Supondo
que a percentagem do distribuidor seja de 28% e os impostos 45%. Escrever um
programa que leia o custo de fábrica de um carro e informe o custo ao consumidor do
mesmo."""

cf = float(input('Valor do carro saído da fábrica: '))
pd = cf*(1+0.28)
ip = pd*(1+0.45)

print(f'Porcentagem da fábrica (28%): R${round(cf*0.28,2)}')
print(f'Valor do carro com a porcentagem da fábrica: R${round(pd,2)}')
print(f'Impostos (45%): R$ {round(pd*0.45,2)}')
print(f'Valor do carro ao consumidor: R$ {round(ip,2)}')
