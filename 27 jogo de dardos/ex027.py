from math import prod

test_cases = int(input())
list_of_moves = []
pontuacao = []

for _ in range(1, test_cases + 1):
    rounds = []
    for _ in range(1, 6 + 1):
        rounds.append(input())
    list_of_moves.append(rounds.copy())
    rounds.clear()

pontos_joao = 0
pontos_maria = 0

for round in list_of_moves:
    for num in round:
        produto = list(num.split(' '))
        for ind, item in enumerate(produto):
            produto[ind] = int(item)
        pontuacao.append(prod(produto, start=1))
    for item in range(0, 3):
        pontos_joao += pontuacao[item]
    for item in range(3, 6):
        pontos_maria += pontuacao[item]
    if pontos_joao > pontos_maria:
        print('JOAO')
    elif pontos_maria > pontos_joao:
        print('MARIA')
    pontuacao.clear()
    pontos_joao = 0
    pontos_maria = 0

