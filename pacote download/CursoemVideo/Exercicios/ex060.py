num = int(input('Digite o numero: '))
contador = num
fatorial = 1
print('{}! = '.format(num), end = '')
while contador > 0 :
  print('{}'.format(contador), end = '')
  print(' x ' if contador > 1 else ' = ', end = '')
  fatorial = fatorial * contador
  contador = contador - 1
print(fatorial)
