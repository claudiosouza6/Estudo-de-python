from random import randint

lista = []
jogos = []
print('-='*30)
print('       JOGA NA MEGA SENA       ')
print('-='*30)
quantidade_jogos = int(input('Quantos jogos quer que eu sorteie? '))
total = 1
while total <= quantidade_jogos:
  contador = 0
  while True: 
    numero = randint(1,60)
    if numero not in lista:
      lista.append(numero)
      contador = contador + 1
    if contador >= 6:
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  total = total + 1
for indice, lista in enumerate(jogos):
  print(f'Jogo {indice + 1}: {lista}')