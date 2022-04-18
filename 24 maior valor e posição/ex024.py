from random import randint
maior = 0
posicao = 0

for num in range(1, 101):
    numero = randint(1, 99999)
    print(numero)
    if numero > maior:
        maior = numero
        posicao = num
print(maior)
print(posicao)
