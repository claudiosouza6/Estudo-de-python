lista = list()

while True:
  nome = (str(input('Nome: ')))
  nota1 = float(input('Primeira nota: '))
  nota2 = float(input('Segunda nota: '))
  media = (nota1 + nota2)/2

  lista.append([nome, [nota1, nota2], media])

  
  continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continuar == 'N':
    break

print('-='*30)
print(lista)
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for indice, aluno in enumerate(lista):
  print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
  print('-'*35)
  opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if opc == 999:
    print('Finalizando...')
    break
  if opc <= len(lista) - 1:
    print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')