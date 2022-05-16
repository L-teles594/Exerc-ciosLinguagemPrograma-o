def somatemp():
    soma = 0
    cont = 1
    while cont <= 30:
        temp = float(input('digite uma temperatura:  '))
        soma += temp
        cont += 1
    return soma


s = somatemp()
print(f'A soma das temperaturas é {s}')