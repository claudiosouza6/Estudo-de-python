'''teste = []
teste.append('Gustavo')
teste.append(40)

galera = []
galera.append(teste[:])           #tem que fazer copia pra nao mudar o valor inicial tambem

teste[0] = 'Maria'
teste[1] = 23
galera.append(teste[:])
print(galera)'''

'''galera = [ ['Joao', 19] , ['Ana', 33] , ['Luna', 17] , ['Baby Yoda', 5] ]
print(galera)
print(galera[0])
print(galera[3][0])
for pessoa in galera:
  print(pessoa)
  print(pessoa[1])
  print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')'''

galera = []
dado = []
total_maior_idade = total_menor_idade = 0
for contador in range(0,5):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  galera.append(dado[:])
  dado.clear()

for pessoa in galera:
  if pessoa[1] >= 21:
    print(f'{pessoa[0]} é maior de idade')
    total_maior_idade = total_maior_idade + 1
  else:
    print(f'{pessoa[1]} é menor de idade')
    total_menor_idade = total_menor_idade + 1

print(galera)
print(f'Temos {total_maior_idade} maiores de idade e {total_menor_idade} menores de idade')