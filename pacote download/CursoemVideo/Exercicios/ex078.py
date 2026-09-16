valores = []
maior = 0
menor = 0

for contador in range(0,5) :
  valores.append(int(input(f'Digite um valor inteiro para a posição {contador}: ')))

  if contador == 0:
    maior =  menor = valores[contador]
  else:  
    if valores[contador] > maior:
      maior = valores[contador]
    if valores[contador]< menor:
      menor = valores[contador]

print('=-'*30)
print(f'Números digitados: {valores}')
print(maior, menor)

for posicao, maior_valor in enumerate(valores):
  if maior_valor == maior:
    print(f'O maior valor foi {maior_valor} na posição {posicao}')

for posicao, menor_valor in enumerate(valores):  
  if menor_valor == menor:
    print(f'O menor valor foi {menor_valor} na posição {posicao}')