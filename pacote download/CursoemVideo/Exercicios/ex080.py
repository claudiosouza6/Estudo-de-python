lista = [] 
contador = 0

for contador in range(0,5):
  numero = int(input('Digite o numero da lista: '))
  if contador == 0 or numero >= lista[-1]:
    lista.append(numero)
    print('Numero adicionado no final da lista!')
  else:
    posicao = 0
    while posicao < len(lista):
      if numero <= lista[posicao]:
        lista.insert(posicao, numero)
        print(f'Adicionado na posicao {posicao} da lista!')
        break
      posicao = posicao + 1

print('='*30)
print(lista)