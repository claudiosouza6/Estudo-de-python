lista = []

while True:
  numero = int(input('Digite o numero: '))
  lista.append(numero)

  pares = [p for p in lista if p % 2 == 0]
  impares = [i for i in lista if i % 2 != 0]

  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continuar == 'N':
    break

print('-='*30)
print(f'Lista completa: {lista}')
print(f'Lista pares: {pares}')
print(f'Lista ímpares: {impares}')