import random

def embaralhar_manual(itens):
    """
    Implementação do Algoritmo de Fisher-Yates (Algoritmo P de Knuth)
    para gerar uma permutação aleatória uniforme.
    """
    total_de_itens = len(itens)
    for posicao_atual in range(total_de_itens - 1, 0, -1):
        # Sorteia um índice posicao_sorteada entre 0 e posicao_atual
        posicao_sorteada = random.randint(0, posicao_atual)
        # Permuta (troca) os elementos nas posições 'posicao_atual' e 'posicao_sorteada'
        itens[posicao_atual], itens[posicao_sorteada] = itens[posicao_sorteada], itens[posicao_atual]
    return itens

# Dados de exemplo: 4 cartas especiais (poderiam ser mais, mas teriam mais possibilidades)
cartas = ["Dragão", "Mago", "Guerreiro", "Arqueiro"]

print(f"Conjunto original: {cartas}")
# O número total de permutações possíveis é 4! = 24
permutacao = embaralhar_manual(cartas.copy())
print(f"Permutação gerada: {permutacao}")