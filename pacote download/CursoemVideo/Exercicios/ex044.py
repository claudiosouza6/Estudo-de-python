print('CALCULAR VALOR A SER PAGO NO PRODUTO' )
print('-=-' * 30)
preco = float(input('Qual o preço do produto: '))
print('''FORMAS DE PAGAMENTO: 
(1) à vista dinheiro/cheque 
(2) à vista cartão 
(3) 2x no cartão 
(4) 3x ou mais no cartão ''')
pagamento = int(input('Qual a opção de pagamento: '))
if pagamento == 1 :
  valor_final = preco - (preco * 10/100)
  print('O valor a ser pago é de R$ {:.2f}'.format(valor_final))
elif pagamento == 2 :
  valor_final = preco - (preco * 5/100)
  print('O valor a ser pago é de R$ {:.2f}'.format(valor_final))
elif pagamento == 3 :
  valor_final = preco
  parcela = valor_final / 2
  print('O valor a ser pago é de R$ {:.2f}'.format(valor_final))
  print('2 parcelas de R$ {:.2f}'.format(parcela))
elif pagamento == 4 :
  valor_final = preco - (preco * 20/100)
  parcelas = int(input('Quantas parcelas: '))
  parcela = valor_final / parcelas
  print('O valor a ser pago é de R$ {:.2f}'.format(valor_final))
  print('{} parcelas de de R$ {:.2f}'.format(parcelas, parcela))
else : 
  print('Opção de pagamento inválida!')
#print('O valor a ser pago é de R$ {:.2f}'.format(valor_final))