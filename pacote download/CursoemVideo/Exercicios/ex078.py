valores = []
maior = 0


for contador in range(0,5) :
  numero = int(input(f'Digite um valor inteiro para a posição {contador}: '))
  valores.append(numero)

  if contador == 0:
    maior = numero
    menor = numero

  else:  
    if numero > maior:
      maior = numero
    if numero< menor:
      menor = numero
  contador = contador + 1

print(f'Números digitados: {valores}')
print(maior, menor)

for posicao, maior_valor in enumerate(valores):
  if maior_valor == maior:
    print(f'O maior valor foi {maior_valor} na posição {posicao}')

for posicao, menor_valor in enumerate(valores):  
  if menor_valor == menor:
    print(f'O menor valor foi {menor_valor} na posição {posicao}')