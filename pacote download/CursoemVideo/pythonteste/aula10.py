# nome = str(input('Qual o seu nome:').strip())
# if nome == 'Claudio':
#   print('Nome bonito seu coiso!')
# else:
#   print('NOME COMUM!')
# print('Bom dia {}!'.format(nome))

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = (nota1 + nota2) / 2
print('A sua media foi {}'.format(media))
if media >= 7:
  print('Aprovado!')
elif media >= 4 and media < 7:
  print('Recuperação!')
else:
  print('Reprovado!')

print('Parabens, não fez mais que a obrigação!' if media >= 7 else ('Precisa estudar mais seu zafado!'))