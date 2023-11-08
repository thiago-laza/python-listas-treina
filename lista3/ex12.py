"""12. Escrever um programa que leia o número de matrícula dos vendedores de uma empresa, seu salário
fixo e o total de vendas de cada vendedor. Cada vendedor recebe um salário fixo, mais uma
comissão proporcional às vendas por ele efetuadas. A comissão é de 3% sobre o total de vendas até
1.000 e 5 % sobre o que ultrapassa este valor. Escrever o número do vendedor, o total de suas
vendas, seu salário fixo e seu salário total. OBS: A leitura deve ser encerrada quando ler a matrícula
do vendedor com número igual a 99."""

cad = 's'

while cad == 's':
    print(10*'-')
    matr = input('Matricula: ')
    sal = float(input('Salario fixo: '))
    ven = float(input('Vendas: '))
    print(10*'-')
    if ven <= 1000:
        sal_fim = sal + 1.03*ven
    else:
        sal_fim = sal + 1.05*ven
    
    print(10*'-')
    print(f'Matricula: {matr}')
    print(10*'-')
    print(f'Vendas: R$ {ven}')
    print(10*'-')
    print(f'Salario fixo: R$ {sal}')
    print(10*'-')
    print(f'Salario total: R$ {sal_fim}')
    print(10*'-')
    cad = input('Deseja cadastrar  mais algum funcionario ? (s/n): ')
    
    if cad == 'n':
        break
