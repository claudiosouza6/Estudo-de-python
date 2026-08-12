numero = quantidade = soma = 0
while True :
  numero = int(input('Digite um numero (999 faz parar): '))
  if numero == 999 :
    break
  quantidade += 1
  soma += numero
print('-='*30)
print(f'Foram digitados {quantidade} valores')
print(f'A soma entre os numeros digitados foi de {soma}')