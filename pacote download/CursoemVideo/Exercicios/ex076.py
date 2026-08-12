contador = 0
tupla = ('bicicleta',500.00,'camisa',60.00,'baby yoda',70.00,'computador',5000.00,'garrafa térmica',55.00,'capivara pelucia',120.00,'mouse bluetooth',115.00)
'''
print('-'*40)
print('LISTAGEM DE PREÇOS')
print('-'*40)

while contador < len(tupla) :
  print(tupla[contador].ljust(30,'.'), 'R$', tupla[contador+1])
  contador += 2


print('-'*40)
'''

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(tupla)) :
  if pos % 2 == 0:
    print(f'{tupla[pos]:.<30}', end='')
  else:
    print(f'R${tupla[pos]:>7.2f}')
print('-'*40)