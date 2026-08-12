soma = 0
contador = 0
for universo in range(0, 6) :
  num = int(input('Digite um numero: '))
  if num % 2 == 0 :
    soma += num
    contador += 1
print('A soma dos {} numeros pares foi de: {}'.format(contador, soma))