nota_trabalhos = float(input())
prova_regular = float(input())
media = (nota_trabalhos + prova_regular) / 2

if media >= 6.00:
    print('aprovado')
else:
    print('talvez com a sub') if (nota_trabalhos + 10) / 2 >= 6 else print('reprovado')
