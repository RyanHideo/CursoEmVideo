from random import randint
from time import sleep
r = randint(0,5)
n = int(input('Qual o numero escolhido? '))
print('PROCESSANDO...')
sleep(3)
if n == r:
    print('Você acertou!')
else:
    print(f'Você errou! eu pensei no numero {r}!')


