notas = list(input().split())

for i, nota in enumerate(notas):
    notas[i] = float(nota)

media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] )/ 10
print(f'MEDIA: {media}')

if media >= 7.0:
    print('Aluno aprovado.')
elif 7 > media >= 5:
    print('Aluno em exame.')
    nota_exame = float(input('Nota do exame: '))
    media = (media + nota_exame ) / 2
    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media}')
else:
    print('Aluno reprovado.')
