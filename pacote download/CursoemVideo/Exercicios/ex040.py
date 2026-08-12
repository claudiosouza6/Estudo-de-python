print('CÁLCULO DE MÉDIA')
n1 = float(input('Diggite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média entre {} e {} é de  {}'.format(n1, n2, media))
if media < 5 :
  print('Sua média final foi de {}, logo está REPOVADO!'.format(media))
elif media > 5 and media <= 6.9 :
  print('Sua média foi de {} logo está de RECUPERAÇÃO!'.format(media))
else :
  print('Sua média foi de {} logo está ATPROVADO! PARABÉNS SEU DISCARADO!'. format(media))