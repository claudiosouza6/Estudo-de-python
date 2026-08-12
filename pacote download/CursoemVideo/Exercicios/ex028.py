from random import randint
from time import sleep
numero = randint(0, 5)
print('-=-'*20)
tentativa = int(input('Tente dizer qual numero a maquina pensou entre 0 e 5: '))
print('LENDO...')
sleep(2)
if tentativa == numero:
  print('Acertou mizeravi!')
else:
  print('ERROU! burrão! o numero certo era {}'.format(numero))
print('-=-'*20)