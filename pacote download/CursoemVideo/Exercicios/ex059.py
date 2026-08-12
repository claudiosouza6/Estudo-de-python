n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
escolha = 0

while escolha != 5 :
  print('----- MENU -----')
  print('''Escolha uma das opções abaixo: 
  [1] SOMAR 
  [2] MULTIPLICAR 
  [3] MAIOR 
  [4] NOVOS NÚMEROS 
  [5] SAIR DO PROGRAMA ''')
  escolha = int(input('Digite sua opção: '))
  if escolha == 1 :
    soma = n1 + n2
    print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
  elif escolha == 2 :
    multiplicaçao = n1 * n2
    print('A multiplicação entre {} e {} é: {}'.format(n1, n2, multiplicaçao))
  elif escolha == 3 :
    if n1 > n2 :
      print('{} é maior que {}'.format(n1, n2))
    elif n2 > n1 :
      print('{} é maior que {}'.format(n2, n1))
    else :
      print('{} e {} são iguais'.format(n1, n2))
  elif escolha == 4 :
    print('Insira os novos números: ')
    n1 = int(input('Insira o primeiro valor: '))
    n2 = int(input('Insira o segundo valor: '))
  elif escolha == 5 :
    print('SAINDO ...')
  else :
    print('Opção inválida!')