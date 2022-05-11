num_inicial = int(input())
num_final = int(input()) + 1
contador = 0

for i in range(num_inicial, num_final):
    conta_divisões = 0
    for j in range(1, i + 1):
        if i % j == 0:
            conta_divisões += 1
    if conta_divisões == 2:
        print(i)
        contador += 1
print(f'primos: {contador}')