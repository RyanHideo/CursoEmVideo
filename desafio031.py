distancia = int(input('Qual a distancia da viagem em Km? '))
if distancia <= 200:
    soma = distancia * 0.50
    print(f'Sua viagem vai sair por {soma}R$! ')
else:
    soma = distancia * 0.45
    print(f'Sua viagem vai sair por {soma}R$! ')