alfabeto = ('', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U'
            'V', 'W', 'X', 'Y', 'Z')

altura = int(input())

for i in range(1, altura + 1):
    print(f'{alfabeto[i]}' * i)
