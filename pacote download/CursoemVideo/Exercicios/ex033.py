numero1 = int(input('Insira o primeiro numero: '))
numero2 = int(input('Insira o segundo numero: '))
numero3 = int(input('Insira o terceiro numero: '))
#VERIFICANDO MAIOR
if numero1 > numero2 and numero1 > numero3 :
  print('O {} é maior que {} e {}!'.format(numero1, numero2, numero3))
elif numero2 > numero1 and numero2 > numero3 :
  print('O {} é maior que {} e {}!'.format(numero2, numero1, numero3))
else :
  print('O {} é maior que {} e {}!'.format(numero3, numero1, numero2))
#VERIFICANDO MENOR
if numero1 < numero2 and numero1 < numero3 :
  print('O {} é menor que {} e {}!'.format(numero1, numero2, numero3))
elif numero2 < numero1 and numero2 < numero3 :
  print('O {} é menor que {} e {}!'.format(numero2, numero1, numero3))
else :
  print('O {} é menor que {} e {}!'.format(numero3, numero1, numero2))