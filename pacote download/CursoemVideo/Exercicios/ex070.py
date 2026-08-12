total_gasto = mais_mil = contador = menor = 0
barato = ''

print('-='*30)
print('-='*30)
print('VAMOS AS COMPRAS')
print('-='*30)

while True :
  print('-='*30)
  nome = str(input('Nome do produto: '))
  preco = float(input('Preço do produto: R$'))
  contador += 1
  total_gasto += preco

  if preco > 1000 :
    mais_mil += 1

  if contador == 1 or preco < menor :
    menor = preco
    barato = nome

  continuar = ''
  while continuar not in ['S', 'N']:
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

  if continuar == 'N' :
    print('Finalizando...')
    break

print('-='*30)
print(f'Total gasto an compra: R${total_gasto:.2f}')
print(f'{mais_mil} produtos custam mais de R$1000,00')
print(f'{barato} foi o produto mais barato')