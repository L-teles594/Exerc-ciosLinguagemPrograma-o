ano_inicial = int(input())
ano_final = int(input()) + 1
contador = 0

for i in range(ano_inicial, ano_final):
    if i % 4 == 0 and i % 100 != 0:
        print(i)
        contador += 1
    elif i % 400 == 0:
        print(i)
        contador += 1

print(f'bissextos: {contador}')