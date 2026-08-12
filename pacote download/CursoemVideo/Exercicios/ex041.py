from datetime import date
ano_atual = date.today().year
print('CONFEDERAÇÃO DE NATAÇÃO QUER SABER SUA IDADE')
ano = int(input('Qual seu ano de nascimento: '))
idade = ano_atual - ano
if idade <= 9 :
  print('Voce tem {} anos, está na categoria MIRIM!'.format(idade))
elif idade > 9 and idade <= 14 :
  print('Voce tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade > 14 and idade <= 19 :
  print('Voce tem {} anos e está na categoria JUNIOR!'.format(idade))
elif idade > 19 and idade <= 20 :
  print('Voce tem {} anos e está na categoria SENIOR!'.format(idade))
else: 
  print('Voce tem {} anos e está na categoria MASTER!'.format(idade))