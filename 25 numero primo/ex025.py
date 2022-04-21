quantidade = int(input())
lista_teste = []

for _ in range(1, quantidade + 1):
    numero = int(input())
    lista_teste.append(numero)

for item in lista_teste:
    divisao = 0
    for num in range(1, item + 1):
        if item % num == 0:
            divisao += 1
    if divisao == 2:
        print(f'{item} eh primo')
    else:
        print(f'{item} nao eh primo')


