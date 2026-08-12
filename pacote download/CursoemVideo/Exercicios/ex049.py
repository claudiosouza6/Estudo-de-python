numero = int(input('Insira o numero que quer a tabuada: '))
for rep in range(1, 11) :
  tabuada = numero * rep
  print('{} * {} = {}'.format(numero, rep, tabuada))