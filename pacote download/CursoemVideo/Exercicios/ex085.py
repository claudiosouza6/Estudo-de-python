lista = [[],[]]

for contador in range(0,7):
  numero = int(input('Digite um número: '))
  if numero % 2 == 0:
    lista[0].append(numero)
  else:
    lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print('=-'*30)
print(lista)
print('=-'*30)
print(f'Numeros pares: {lista[0]}')
print(f'Numeros impares: {lista[1]}')