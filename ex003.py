nome = input('digite algo: ')
print('O tipo primitivo desse valor e ', type(nome))
print('Só tem espacos? ', nome.isspace())
print('É um numero? ', nome.isnumeric())
print('É alfanumerico? ', nome.isalnum())
print('Está em maiusculas? ', nome.isupper())
print('Está em minúscula? ', nome.islower())
print('Está capitalizada? ', nome.istitle())