lista = []
pesadas = []
leves = []
maior = menor = 0
quantidade_pessoas = 0

while True :
  nome = str(input('Digite o nome: '))
  peso = float(input('Digite o seu peso: '))
  lista.append([nome,peso])

  if len(lista) == 1:
    menor = menor = peso
    pesadas.append([nome,peso])
    leves.append([nome,peso])

  else:
    if peso > maior:
      maior = peso
      pesadas.clear()
      pesadas.append([nome,peso])
    elif peso == maior:
      pesadas.append([nome,peso])
      

    else:
      if peso < menor:
       menor = peso
       leves.clear()
       leves.append([nome,peso])
      elif peso == menor:
        leves.append([nome,peso])

  quantidade_pessoas = quantidade_pessoas + 1

  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continuar == 'N':
    break

print('=-'*30)
print(f'A) Pessoas cadastradas = {quantidade_pessoas}')
print(f"B) Pessoa mais pesada pesa {pesadas[0][1]}Kg. Peso de {pesadas[0][0]}")
print(f'C) Pessoa mais leve pesa {leves[0][1]}Kg. Peso de {leves[0][0]}')
