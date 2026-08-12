maior = 0
menor = 0
for pessoas in range(1,6) :
  peso = float(input('Digite o peso: '))
  if pessoas == 1 :
    maior = peso
    menor = peso
  else :
    if peso < menor :
      menor = peso
    if peso > maior :
     maior = peso
print('O maior peso foi: {}'.format(maior))
print('O menor peso foi: {}'.format(menor))