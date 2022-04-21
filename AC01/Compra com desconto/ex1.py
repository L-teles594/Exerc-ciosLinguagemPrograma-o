valor_unitario = float(input())
quantidade_comprada = int(input())
desconto_total = (10 + quantidade_comprada) / 100
valor_total = valor_unitario * quantidade_comprada
valor_final = (valor_unitario * quantidade_comprada) * (1 - desconto_total)
print(f'{valor_total:.2f}')
print(f'{valor_final:.2f}')
