n1 = int(input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
n3 = int(input('Digite o terceiro numero inteiro: '))
if n1>n2>n3:
    print(f'Seu maior numero é {n1} e seu menor numero é {n3}')
elif n3>n2>n1:
    print(f'Seu maior numero é {n3} e seu menor numero é {n1}')
elif n2>n1>n3:
    print(f'Seu maior numero é {n2} e seu menor numero é {n3}')
elif n2>n3>n1:
    print(f'Seu maior numero é {n2} e seu menor numero é {n1}')
elif n3>n1>n2:
    print(f'Seu maior numero é {n3} e seu menor numero é {n2}')
elif n1>n3>n2:
    print(f'Seu maior numero é {n1} e seu menor numero é {n2}')

else:
    print('Dois ou mais numero são iguais!')
