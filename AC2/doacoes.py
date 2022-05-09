vic_coins = 0

while True:
    doacao = float(input())
    if doacao < 0:
        break
    else:
        vic_coins += doacao

doacao_em_real = vic_coins * 2.5

print(f'VC$ {vic_coins:.2f}')
print(f'R$ {doacao_em_real:.2f}')
