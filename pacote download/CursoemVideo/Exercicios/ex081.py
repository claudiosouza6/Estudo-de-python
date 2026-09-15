lista = []
quantidade = 0

while True:
  numero = int(input('Digite um numero: '))
  lista.append(numero)
  quantidade = quantidade + 1
  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continuar == 'N':
    break

lista.sort(reverse=True)

print('=-'*30)
print(f'A) Foram digitados {quantidade} numeros')
print(f'B) Lista ordenada de forma descrescente: {lista}')
if 5 in lista:
  print('C) O valor 5 foi digitado e está na lista')
else:
  print('C) O valor 5 não foi digitado e não está na lista')