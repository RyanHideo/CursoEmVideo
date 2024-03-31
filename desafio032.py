
ano = int(input('Digite um ano: '))
resul = ano % 4
if resul == 0:
    print(f'O ano de {ano} é bissexto!')
else:
    print(f'O ano de {ano} não é bissexto!')
