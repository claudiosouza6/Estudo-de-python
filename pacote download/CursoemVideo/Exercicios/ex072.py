extenso = ('zero', 'um', 'dois','tres','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')

while True :
  numero = int(input('Digite um número por extenso de 0 a 20: '))
  if numero >= 0 and numero <= 20 :
    print (f'Você digitou o número {extenso[numero]}')
    break
  else :
    print('Entrada inválida! Digite um número entre 0 e 20: ')
