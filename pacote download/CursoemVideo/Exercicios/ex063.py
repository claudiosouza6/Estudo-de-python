contador = 0
n = int(input('Quantos numeros de Fibonacci quer: '))
lista = []
while contador < n :
  if contador == 0 :
    lista.append(0)
  elif contador == 1 :
    lista.append(1)
  else :
    lista.append(lista[-1] + lista[-2])
  contador += 1
print('Numeros de Fibonacci: {}'.format(lista))
  