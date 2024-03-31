import math
ca = float(input('Insira o comprimento do cateto adjacente: '))
co = float(input('Insira o comprimento do cateto oposto: '))
hip = math.hypot(ca, co)
print(f'O Comprimento da sua hipotenusa é {hip}')