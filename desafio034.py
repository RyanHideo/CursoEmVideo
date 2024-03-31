sal = float(input('Digite o salario do funcionario: '))
if sal >= 1250.00:
    ajuste = sal*1.1
    print(f'O novo salario do funcionario é de {ajuste:.2f}R$! ')
else:
    ajuste = sal*1.15
    print(f'O novo salario do funcionario é de {ajuste:.2f}R$! ')
