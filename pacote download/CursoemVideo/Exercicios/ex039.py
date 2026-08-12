from datetime import date
ano_atual = date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano
if idade < 18 :
  print('Voce tem {} anos e ainda vai falta {} anos para se alistar no serviço militar!'.format(idade, 18 - idade))
elif idade == 18 :
  print('Voce tem {} e está na hora de se alisatar no servico militar, voce ja tem 18 anos safado!'.format(idade))
else :
  print('Voce tem {} e ja passou do tempo de se alistar no serviço militar, deveria ter se alistado a {} anos atrás!'.format (idade, idade - 18))