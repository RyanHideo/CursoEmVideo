import math

ang = int(input('Insira o seu angulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print(f'O seu angulo {ang}, tem como valores o seno de {sen:.2f}, o cosseno de {cos:.2f} e a tangente de {tan:.2f}')
