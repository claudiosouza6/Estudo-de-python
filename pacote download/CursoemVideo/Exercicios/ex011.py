largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('A área da parede é de {} m² e serão necessarios {} litros de tinta.'.format(area, tinta))