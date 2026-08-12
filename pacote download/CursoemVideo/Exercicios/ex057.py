sexo = str(input('Digite o sexo da pessoa:[M/F] ')).strip().upper()[0]
while sexo not in 'MmFf' :
  sexo = str(input('Dados inválidos. Por favor informe seu sexo[M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
