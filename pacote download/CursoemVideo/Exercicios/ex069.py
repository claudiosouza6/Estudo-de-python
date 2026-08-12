maisdezoito = homens = mulheres = menosvinte = 0
print('-' * 30)
print('----- CADASTRE UMA PESSOA -----')
print('-' * 30)

while True :
  print('-' * 30)
  idade = int(input('Idade: '))
  
  if idade > 18 :
    maisdezoito += 1
  
  while True :
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo in ['M', 'F'] : 
      break
  
  print('-' * 30)
  
  if sexo == 'M' :
    homens += 1
    
  elif sexo == 'F' and idade < 20 :
    menosvinte += 1

  while True :  
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in ['S', 'N'] :
      break

  if continuar == 'S' :
    continue
  elif continuar == 'N' :
    print('Encerrando...')
    break

print('-=' * 30)
print(f'Pessoas com mais de 18 anos: {maisdezoito}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {menosvinte}')