numero = (str(input('Digite um numero entre 0 e 9999: ').zfill(4)))
print('Analisando o numero {}'.format(numero))
lista = [numero[0], numero[1], numero[2], numero[3]]
print('unidade: {}'.format(numero[3]))
print('dezena: {}'.format(numero[2]))
print('centena: {}'.format(numero[1]))
print('milhar: {}'.format(numero[0]))
