ponto_a = list(input().split(' '))
ponto_b = list(input().split(' '))

x1 = float(ponto_a[0])
x2 = float(ponto_b[0])
y1 = float(ponto_a[1])
y2 = float(ponto_b[1])

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'{distancia:.4f}')
