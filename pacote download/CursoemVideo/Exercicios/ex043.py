print('IMC')
print('-=-' * 30)
peso = float(input('Qual o seu peso (em Kg): '))
altura = float(input('Qual a sua altura (em metros): '))
imc = peso / (altura ** 2)
if imc < 18.5 :
  print('Seu IMC é de {:.2f} e voce está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25 :
  print('Seu IMC é de {:.2f} e voce está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30 :
  print('Seu IMC está de {:.2f} e voce está com sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40 :
  print('Seu IMC está de {:.2f} e voce está com obesidade!'.format(imc))
else : 
  print('Seu IMC é de {:.2f} e voce está com obesidade mórbida!'.format(imc))