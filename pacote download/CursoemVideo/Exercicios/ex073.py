tabela = ('palmeiras', 'flamengo','fluminense','athletico','bragantino','bahia','coritiba','sao paulo','atleticoMG','corintians','cruzeiro','botafogo','vitoria','internacional','santos','gremio','vasco','remo','mirassol','chape')

print(f'Lista de times do Campeonato Brasileiro de futebol: {tabela}')
print('-='*40)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-='*40)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*40)
for posicao, time in enumerate(tabela) :
  if time == 'chape':
    print(f'A Chapecoense está na {posicao} posição')