numero_dado = int(input())
impar = numero_dado - 1 if numero_dado % 2 == 0 else numero_dado - 2
par = numero_dado + 2 if numero_dado % 2 == 0 else numero_dado + 1
print(impar, par)
