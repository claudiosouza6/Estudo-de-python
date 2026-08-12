lado1 = float(input('Insira o primeiro lado do triangulo: '))
lado2 = float(input('Insira o segundo lado do triangulo: '))
lado3 = float(input('Insira o terceiro lado do triangulo: '))
print('-=-' * 30)
if(lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1 :
  print('Os lados {}, {} e {} FORMAM um triangulo!'.format(lado1, lado2, lado3))
else :
  print('Os lados {}, {} e {} NÃO FORMAM triangulo!'.format(lado1, lado2, lado3))