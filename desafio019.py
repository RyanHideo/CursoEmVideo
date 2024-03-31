import random
n1 = input('Insira o primeiro nome: ')
n2 = input('Insira o segundo nome: ')
n3 = input('Insira o terceiro nome: ')
n4 = input('Insira o quarto nome: ')
lista = [n1,n2,n3,n4]
sorteio = random.choice(lista)
print(f'O aluno sorteado foi: {sorteio}')
