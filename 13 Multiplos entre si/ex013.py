valores = list(input().split(' '))

a = int(valores[0])
b = int(valores[1])

if a < 0:
    a *= -1
if b < 0:
    b *= -1
print(a, b)

if b > a and b % a == 0:
    print('Sao Multiplos')
elif a > b and a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
