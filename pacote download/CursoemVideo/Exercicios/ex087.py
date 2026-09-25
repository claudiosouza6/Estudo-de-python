matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_par = 0
soma_terceira = 0


for linha in range (0,3):
  for coluna in range (0,3):
   matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

   if matriz[linha][coluna] % 2 == 0:
     soma_par = soma_par + matriz[linha][coluna]

for linha in range (0,3):
  soma_terceira = soma_terceira + matriz[linha][2]

maior_terceira = max(matriz[1])  


print('=-'*30)
for linha in range (0,3):
  for coluna in range (0,3):
    print(f'[{matriz[linha][coluna]:^5}]', end = '')
  print()

print('=-'*30)
print(f'A) Soma dos valores pares = {soma_par}')
print(f'B) Soma dos valores da terceira coluna = {soma_terceira}')
print(f'C) O maior da terceira linha = {maior_terceira}')