quantidade = int(input())
lista_teste = []

for _ in range(1, quantidade + 1):
    numero = int(input())
    lista_teste.append(numero)

for item in lista_teste:
    soma_divisores = 0
    for num in range(1, item):
        if item % num == 0:
            soma_divisores += num
    if item == soma_divisores:
        print(f'{item} eh perfeito')
    else:
        print(f'{item} nao eh perfeito')

