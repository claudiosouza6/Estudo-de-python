primeiro = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razão da PA: '))
progressao = primeiro
termos = []
for PA in range(0, 10) :
  termos.append(progressao)
  progressao = progressao + razao
print('os 10 primeiros termos da progressao: {}'.format(termos))