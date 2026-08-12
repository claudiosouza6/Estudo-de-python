numero = int(input('Insira um numero: '))
base = str(input('''Qual base de conversão você quer: 
(1)binário
(2)octal
(3)hexadecimal '''))
if base == '1':
    print('O número {} em binário é: {}'.format(numero, bin(numero)[2:]))
elif base == '2':
    print('O número {} em octal é: {}'.format(numero, oct(numero)[2:]))
elif base == '3':
    print('O número {} em hexadecimal é: {}'.format(numero, hex(numero)[2:].upper()))
else:
    print('Opção inválida. Escolha 1, 2 ou 3.')
