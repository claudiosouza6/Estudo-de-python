from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print('O computador escolheu {}!'.format(item[computador]))
print('Jogador jogou {}!'.format(item[jogador]))
print('-=' * 20)
if computador == 0 : #computador jogou PEDRA
  if jogador == 0 :
    print('Empate!')
  elif jogador == 1 :
    print('Jogador Vence!')
  elif jogador == 2 :
    print('Computador Vence!')
  else :
    print('Jogada inválida!')
elif computador == 1 :     #computador jogou PAPEL
  if jogador == 0 :
    print('Computador Vence!')
  elif jogador == 1 :
    print('Empate!')
  elif jogador == 2 :
    print('Jogador Vence!')
  else :
    print('Jogada Inválida!')

elif computador == 2 :     #computador jogou TESOURA
  if jogador == 0 :
    print('Jogador Vence!')
  elif jogador == 1 :
    print('Computador Vence!')
  elif jogador == 2 :
    print('Empate!')
  else :
    print('Jogada Inválida!')
print('-=' * 20)