from random import randint
from time import  sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Você perdeu!')
    elif jogador == 2:
        print('Você ganhou!')
    else:
        print('Opção invalida!')
elif computador == 1:
    if jogador == 0:
        print('Você perdeu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Você perdeu!')
    else:
        print('Opção invalida!')
elif computador == 2:
    if jogador == 0:
        print('Você ganhou!')
    elif jogador == 1:
        print('Você perdeu!!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Opção invalida!')
