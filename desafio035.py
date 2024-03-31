l1 = float(input('Qual o tamanho do primeiro lado: '))
l2 = float(input('Qual o tamanho do segundo lado: '))
l3 = float(input('Qual o tamanho do terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel formar um triangulo!')
