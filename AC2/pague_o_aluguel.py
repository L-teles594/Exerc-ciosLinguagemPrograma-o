divida = int(input())
pagamento_mensal = int(input())
pagamentos = 1


while divida > 0:
    print(f'pagamento: {pagamentos}')
    print(f'antes = {divida}')
    if pagamento_mensal > divida:
        divida = 0
    else:
        divida -= pagamento_mensal
        pagamentos += 1
    print(f'depois = {divida}')
    print('-----')
