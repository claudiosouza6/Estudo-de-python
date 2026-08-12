numero = contador = tabuada = 0
while True :
  numero = int(input('Digite o valor para a tabuada (numero negativo faz parar): '))
  if numero < 0 :
    break
  contador = 0
  while contador <= 10 :
    tabuada = numero * contador
    print(f'{numero} * {contador} = {tabuada}')
    contador += 1
    
print('FIM')