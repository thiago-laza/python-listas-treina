"""3.Elabore um programa que receba o nome de um aluno e verificar se ele
existe o sobrenome “SILVA”."""

nome = input('Digite seu nome: ')

if 'silva' in nome:
    print(f'O aluno {nome} tem silva')
else:
    print(f'O aluno {nome} nao tem silva')