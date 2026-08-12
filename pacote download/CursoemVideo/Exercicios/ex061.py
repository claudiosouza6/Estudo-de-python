primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
contador = 0
progressao = primeiro
termos = []
while contador < 10 :
  termos.append(progressao)
  progressao = progressao + razao
  contador += 1
print('-=' * 20)
print('''Os 10 primeiros termos da PA de razão {} começando em {} são:
{} '''.format(razao, primeiro, termos))