distancia = float(input('Qual a distancia da viagem em km: '))
if distancia<= 200 :
  preço = distancia *0.50
  print('A viagem com {} km de distancia fica com o preço de R$ {:.2f}'.format(distancia, preço))
else :
  preço = distancia * 0.45
  print('A viagem com {} km de distancia fica com o preço de R$ {:.2f}'.format(distancia, preço))