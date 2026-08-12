valor = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o salário do comprador: R$ '))
anos = int(input('Em quantos anos vai pagar: '))
valorMensal = valor / (anos * 12)
if valorMensal > salario * (30/100) :
  print('Empréstimo negado! O valor corresponde a {:.2f}% do salário'.format(valorMensal / salario * 100))
else :
  print('Empréstimo aprovado! PARABENS SEU SACANA! O valor corresponde a {:.2f}% do salário'.format(valorMensal / salario * 100))
print('vai pagar R$ {:.2f} por mês se tiver um salario de R$ {:.2f} o valor da casa de R$ {:.2f}'.format(valorMensal, salario, valor))