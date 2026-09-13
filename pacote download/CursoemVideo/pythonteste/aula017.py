#LISTAS
"""
num = [2, 5, 9, 1]
num[2] = 3                  #NA LISTA TROCA VALOR
num.append(7)              #adiciona valor no final da lista
num.sort()                   #colocou em ordem
num.sort(reverse = True)         #a lista inverte
num.insert(2, 0)            #insere na posição "2" o valor "0"
num.pop()             #remove o último valor da lista
num.pop(3)              #remove o quarto valor (0,1,2,'3')
num.remove(2)         #vai procurar na lista o primeiro valor "2" e vai remover ele (se tiver mais de um nao remove)
if 4 in num:
  num.remove(4)
else:
  print('Não tem o número 4')       # busca na lista numero pra remover, se n tiver mostra a frase

print(num)
print(f'essa lista tem {len(num)} elementos')         #len = quantos itens tem a lista

"""


'''
valores = []
valores.append(5)
valores.append(9)
valores.append(4)          #5, 9, 4 valores PREDEFINIDOS

for posicao, valor in enumerate(valores):       #o enumerate vai pegar c e valor e dividir em: (posição e valor)
  print(f'Na posição {posicao} encontrei o valor {valor}!')
print('Final da lista')
'''

'''
valores = []
for contador in range(0,5):
  valores.append(int(input('Digite um valor: ')))      #pega o valor que usuario quer e coloca na lista

for posicao, valor in enumerate(valores):       #o enumerate vai pegar c e valor e dividir em: (posição e valor)
  print(f'Na posição {posicao} encontrei o valor {valor}!')
print('Final da lista')
'''

a = [2,3,4,7]
b = a[:]             #o [:] faz o b criar uma CÓPIA de a, logo ao alterar b não altera a
b[2] = 8            #se igualar lista altera o "a" também

print(f'Lista A: {a}')
print(f'Lista B: {b}')