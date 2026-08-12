soma = 0
contador = 0
for num in range (1, 501, 2) :
  if num % 3 == 0 :
    contador +=  1
    soma +=  num
print('A soma de {} valores solicitados é: {}'.format(contador, soma))