"""5.Faça um programa que lê uma string e imprima “É um Palíndromo” caso a
string seja um palíndromo e “Não é palíndromo” caso não seja. A entrada
não tem acentos e que todas as letras são minúsculas. Exemplos de
palíndromo: “ovo”, “reviver”, “mega bobagem”, “anotaram a data da
maratona”"""

palavra = str(input('Digite uma palavra para ver se e um palindromo: '))
palindromo = palavra[::-1]

if palavra == palindromo:
    print(f'A palavra {palavra} e um palindromo.')
else:
    print(f'A palavra {palavra} nao e um palindromo.')