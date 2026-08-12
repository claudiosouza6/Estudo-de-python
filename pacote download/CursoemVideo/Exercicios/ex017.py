from math import hypot
catetoOposto = float(input('Informe o comprimento do cateto oposto do triangulo retangulo: '))
catetoAdjacente = float(input('Informe o comprimento do cateto adjacente do triangulo retangulo: '))
print('O comprimento da hipotenusa do triangulo retangulo de cateto oposto {} e cateto adjacente {} é de {:.2f}'.format(catetoOposto, catetoAdjacente, hypot(catetoOposto, catetoAdjacente)))