dias_da_semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado' )
dia_da_compra = input()
dias_para_entregar = int(input())
dia_da_entrega = dias_da_semana.index(dia_da_compra) + dias_para_entregar
print('chega hoje!') if dias_para_entregar == 0 else print('sera entregue', dias_da_semana[dia_da_entrega])
