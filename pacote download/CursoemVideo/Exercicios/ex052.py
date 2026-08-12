numero = int(input('Digite um numero: '))
if numero < 2 :
  print('{} não é primo!'.format(numero))
else :
  for x in range (2, int(numero**0.5) + 1) :
    if numero % x == 0 :
      print('{} não é primo!'.format(numero))
      break
  else :
    print('{} é primo!'.format(numero))