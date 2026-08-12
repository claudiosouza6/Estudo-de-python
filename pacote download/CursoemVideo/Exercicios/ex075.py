tupla = ()
noves = 0 

print('=-'*40)
print('Serão guardados 4 valores numéricos')
print('=-'*40)

for contador in range (0, 4): 
  valor = int(input(f'Qual o {contador + 1} valor: ')) 
  tupla = tupla + (valor, )
  if valor == 9 :
    noves = noves + 1

print('=-'*40)
print(f'Voce digitou os valores: {tupla}')
print(f'O valor 9 apareceu {noves} vezes')

for posicao, tres in enumerate(tupla) :
    if tres == 3 :
      print(f'O valor 3 apareceu na {posicao + 1} posicao')