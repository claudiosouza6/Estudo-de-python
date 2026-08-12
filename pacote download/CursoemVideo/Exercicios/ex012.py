preco = float(input('Digite o preço do produto: '))
print('Preço antigo do produto: R$ {:.2f}\nPreço novo do produto com 5% de desconto: R$ {:.2f}'.format(preco, preco - (preco * 5/100)))