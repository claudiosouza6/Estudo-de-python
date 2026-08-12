frase = str(input('Digite uma frase? ')).upper().strip()
print('A letra A aparece {} vezes na frase!'.format(frase.count('A')))
print('A aparece pela primeira vez na posição {}! (contando espaços)'.format(frase.find('A')+1))
print('A aparece pela ultima vez na posição {}! (contando espaços)'. format(frase.rfind('A')+1))