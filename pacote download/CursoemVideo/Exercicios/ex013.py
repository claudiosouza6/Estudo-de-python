salario = float(input('Qual o salário: R$'))
print('Salário antigo: R$ {:.2f}\nSalário novo com aumento de 15%: R${:.2f}'.format(salario, salario + (salario * 15/100)))