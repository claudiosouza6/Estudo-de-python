from random import randint

numeros_aleatorios = (randint(0, 10) for _ in range (0, 5))

listagem = tuple(numeros_aleatorios)
print(f"Lista de numeros: {listagem}")

print(f'O menor valor foi {min(listagem)}')
print(f'O maior valor foi {max(listagem)}')