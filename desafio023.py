num = int(input('Informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisand o numero {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centana: {c}')
print(f'Milhar: {m}')
