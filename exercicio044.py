print('='*10, 'LOJA DO RYAN', '='*10)
valor = float(input('Preço das compras: '))
if valor != 0:
    op = int(input('''
    [1] à vista dinheiro/cheque 
    [2] à vista no cartão
    [3] 2x no cartão
    [4] 3x ou mais no cartão
    Qual é a opção? '''))
    if op == 1:
        total = (valor*90)/100
        print(f'O valor a ser pago é de {total}')
    elif op == 2:
        total = (valor*95)/100
        print(f'O valor a  ser pago é de {total}')
    elif op == 3:
        print(f'O valor a ser pago é de {valor}')
    elif op == 4:
        total = (valor*120)/100
        print(f'O valor a ser pago é de {total}')
    else:
        total = 0
        print('Opção invalida de pagamento.')