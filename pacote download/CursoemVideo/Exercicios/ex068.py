from random import randint
vitorias = 0
print('=-' * 30)
print('JOGO DE PAR OU ÍMPAR')
print('=-' * 30)
while True :
  pc = randint(0, 10)
  valor = int(input('Digite um valor: '))
  escolha = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
  total = pc + valor
  if escolha not in ('P','I') :
    print('Opção Inválida! Escolha Par ou ímpar [P/I]')
    continue
  elif escolha == 'P' and (total % 2 == 0):
    vitorias += 1
    print(f'Voce jogou {valor} e o PC jogou {pc}. O total deu {total} e é PAR')
  if escolha == 'I' and (total % 2 != 0) :
    vitorias += 1
    print(f'Voce jogou {valor} e o PC jogou {pc}. O total deu {total} e é ÍMPAR')
  else :
    print(f'Voce jogou {valor} e o PC jogou {pc}. O total deu {total} e você PERDEU')
    break
print(f'GAME OVER! Você venceu {vitorias} vezes.')