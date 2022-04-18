count = 0
soma = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    soma += idade
    count += 1
if count > 0:
    media = soma / count
    print(f'{media:.2f}')

