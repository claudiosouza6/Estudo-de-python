lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#lanche = ('hamburguer')
print(lanche)
print(lanche[1])
print(lanche[1:3])    #1 até o 3 (desconsidera o ultimo. ou seja 1 e 2)
print(lanche[2:]) 

for comida in lanche :
  print(f'Eu vou comer {comida}')
print('Acabei de comer!')

for contador in range(0, len(lanche)) :
  print(f'Eu comi {lanche[contador]}')
print('Eu acabei de comer!!')

for posicao, comida in enumerate(lanche) :
  print(f'Eu comi {comida} na posicao {posicao}')
print('Eu acabei de comer!!')

a = (2, 5, 4)
b= (5, 8, 1, 2)
c = a + b
print(c)

pessoa = ('Gustavo', 39, 'M', 99.88)

print(pessoa)
