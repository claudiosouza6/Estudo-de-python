from random import randint
from time import sleep
tentativa = 0
palpites = 0
numero = randint(0, 10)
print('-=-'*20)
print('Sou seu computador ... Acabei de pensar em um numero entre 0 e 10 :)')
print('Será que voce consegue adivinhar qual foi?')
acertou = False
# while tentativa != numero :
#   tentativa = int(input('Tente dizer qual numero a maquina pensou entre 0 e 10: '))
#   print('LENDO...')
#   sleep(2)
#   if tentativa == numero:
#     print('Acertou mizeravi!')
#   else:
#     print('ERROU! burrão! TENTE NOVAMENTE')
#     print('-=-'*20)
while not acertou :
  jogador = int(input('Qual é seu palpite: '))
  palpites += 1
  if jogador == numero :
    acertou = True
print('Acertou com {} tentativas!'.format(palpites))
print('-=-'*20)

