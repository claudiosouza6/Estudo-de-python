soma_idades = 0
mulheres_menores_vinte = 0
maior_idade_homem = 0
mais_velho = ''

for pessoas in range(1,5) :
  print('----- {}ª PESSOA -----'.format(pessoas))
  nome = str(input('Digite o nome: '))
  idade = int(input('Digite a idade: '))
  sexo = str(input('Digite o sexo (M) ou (F): ')).upper()
  soma_idades += idade
  if sexo == 'M' :
    if idade > maior_idade_homem :
      maior_idade_homem = idade
      mais_velho = nome
  else :
    if sexo == 'F' and idade < 20 :
      mulheres_menores_vinte += 1
media = soma_idades / 4
print('A média de idade do grupo é de {:.1f} anos!'.format(media))
if mais_velho :
  print('O nome do homem mais velho é: {}'.format(mais_velho))
else :
  print('Não tem nenhum homem no grupo!')
print('{} mulheres tem menos de 20 anos'.format(mulheres_menores_vinte))