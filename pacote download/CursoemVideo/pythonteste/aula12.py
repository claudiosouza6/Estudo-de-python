nome = str(input('Qual o seu nome: ')).strip()
if nome == 'Claudio' :
  print('Que nome topzera!')
elif nome == 'Luna' or nome == 'Milka' :
  print('Nome melhor de todos parabains!')
elif nome in 'Lucio Estela Karina' :
  print('Show de bola familia bids!')
else :
  print('Seu nome não é nada demais!')
print('Tenha uma boa noite {}!'.format(nome))