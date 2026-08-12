import math
angulo = float(input('Digite o valor do angulo: '))
# radiano = math.radians(angulo)
# print('O valor do seno do angulo {} é de {}'.format(angulo, math.sin(radiano)))
# print('O valor do coseno do angulo {} é de {}'.format(angulo, math.cos(radiano)))
# print('O valor da tangente do angulo {} é de {}'.format(angulo, math.tan(radiano)))

print('O valor do seno do angulo {:.2f} é de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O valor do coseno do angulo {:.2f} é de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O valor da tangente do angulo {:.2f} é de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))


