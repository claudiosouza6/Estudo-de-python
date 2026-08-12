salario = float(input('Qual o salario atual: '))
if salario > 1250 :
  novo = salario + (salario * 10/100)
  #print('O salário foi aumentado de R$ {:.2f} para R$ {:.2f}!'.format(salario, novo))
else :
  novo = salario + (salario * 15/100)
  #print('O salário foi aumentado de R$ {:.2f} para R$ {:.2f}!'.format(salario, novo))
print('O salário foi aumentado de R$ {:.2f} para R$ {:.2f}!'.format(salario, novo))