soma = 0
quantos = 0
n = int(input('Digite um numero (999 para): '))
while n != 999 :
  soma += n
  quantos += 1
  n = int(input('Digite um numero (999 para): '))
print('-=' * 20)
print('Numeros digitados: {}'.format(quantos))
print('Soma entre os números: {}'.format(soma))
print('-=' * 20)
print('ENCERRADO')