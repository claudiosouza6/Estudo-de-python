from datetime import datetime
ano = datetime.now().year
menores = 0
maiores = 0
for pessoas in range(1,8):  
  nasc = int(input('Digite o ano de nascimento da {} pessoa: '.format(pessoas)))
  idade = ano - nasc
  if idade < 18 :
    menores += 1
  else :
    maiores += 1
print('Entre as 7 pessoas {} são menores de idade e {} são maiores de 18 anos!'.format(menores, maiores))