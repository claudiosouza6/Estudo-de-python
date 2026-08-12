velocidade = float(input('Qual a velocidade do carro: '))
if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('Voce acaba de ser MULTADO! Precisa pagar o valor de R${} por estar a {} km/h'.format(multa, velocidade))