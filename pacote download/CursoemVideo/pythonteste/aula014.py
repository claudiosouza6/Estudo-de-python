# contador = 1
# while contador < 10 :
#   print(contador)
#   contador += 1
# print('FIM!')

# n = 1
# while n != 0 :
#   n = int(input('Digite um numero: '))
# print('FIM do teste')

# resposta = 'S'
# while resposta == 'S' :
#   numero = int(input('Digite o valor: '))
#   resposta = str(input('Quer continuar:[S/N] ')).strip().upper()
# print('FIM')

n = 1
par = impar = 0
while n != 0 :
  n = int(input('Digite o numero: '))
  if n != 0 :
    if n % 2 == 0 :
      par += 1
    else :
      impar += 1
print('Voce digitou {} numeros pares e {} numeros impares!'.format(par, impar))