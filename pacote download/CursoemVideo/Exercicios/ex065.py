maior = menor = quantidade = soma = 0
resposta = ''
n = int(input('Digite um numero: '))
menor = maior = n
while resposta != 'N' :
  quantidade += 1
  soma += n
  if n > maior :
    maior = n
  if n < menor :
    menor = n
  resposta = str(input('Gostaria de continuar [S/N]: ')).strip().upper()[0]
  if resposta != 'N' :
    n = int(input('Digite um numero: '))
media = soma / quantidade
print('''
      QUANTIDADE = {}
      SOMA = {}
      MÉDIA = {}
      MAIOR = {}
      MENOR = {}
      '''.format(quantidade, soma, media, maior, menor))
print('FIM')