salas = []
while True:
    matriculas = []
    numero_de_alunos = int(input())
    for _ in range(0, numero_de_alunos):
        matriculas.append(input())
    salas.append(matriculas.copy())
    print(salas)
