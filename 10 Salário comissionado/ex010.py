nome_vendedor = str(input())
salario_fixo = float(input())
valor_em_vendas = float(input())
salario_final = salario_fixo + valor_em_vendas * 0.15
print(f'TOTAL = R$ {salario_final:.2f}')
