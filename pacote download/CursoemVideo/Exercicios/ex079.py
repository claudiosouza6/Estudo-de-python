'''
lista = []

while True:
  numero = int(input('Digite um número inteiro(-1 para parar): '))
  if numero == -1:
    break
  if numero in lista:
    continue
  else:
    lista.append(numero)

lista.sort()
print(f'Valores únicos em ordem crescente: {lista}')
'''

lista = []

while True:
  numero = int(input('Digite um número: '))
  if numero in lista:
    print('Valor duplicado! Não adicionado na lista!')
  else:
    lista.append(numero)
    print('Valor adicionado na lista!')

  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

  while continuar not in 'SN':
     continuar = str(input('Opção inválida! Quer continuar? [S/N] ')).strip().upper()[0]

  if continuar == 'N':
    break
print('='*30)
lista.sort()
print(f'Valores únicos em ordem crescente: {lista}')