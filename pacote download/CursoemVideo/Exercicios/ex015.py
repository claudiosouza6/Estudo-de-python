quilometros = int(input('Quantos quilometros percorridos: '))
dias = int(input('Quantos dias de aluguel: '))
print('Com {} quilometros percorridos e {} dias de aluguel, o valor a pagar é de R${:.2f}'.format(quilometros, dias, (quilometros * 0.15) + (dias * 60)))