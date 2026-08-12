from random import shuffle
aluno1 = str(input('Nome do aluno 1: '))
aluno2 = str(input('Nome do aluno 2: '))
aluno3 = str(input('Nome do aluno 3: '))
aluno4 = str(input('Nome do aluno 4: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem dos alunos sorteados foi? {}'.format(lista))