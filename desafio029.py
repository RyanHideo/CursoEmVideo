vel = int(input('Qual a velocidade do carro: '))
if vel <= 80:
    print('Voce esta dentro do limite de velocidade!')
else:
    multa = (vel - 80) * 7
    print(f'você estava a {vel} e foi multado em {multa}R$')
