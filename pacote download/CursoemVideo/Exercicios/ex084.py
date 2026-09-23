lista = []
pesadas = []
leves = []
quantidade_pessoas = 0

while True :
  nome = str(input('Digite o nome: '))
  peso = float(input('Digite o seu peso: '))
  lista.append([nome,peso])
  quantidade_pessoas = quantidade_pessoas + 1


  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continuar == 'N':
    break

print('=-'*30)
print(lista)
print(f'A) Pessoas cadastradas = {quantidade_pessoas}')
print("B) Pessoas mais pesadas = {}")
print('C) Pessoas mais leves = {}')
