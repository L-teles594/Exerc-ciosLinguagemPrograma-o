x = 100
y = 200
i = 0
bom_dia = 0
boa_tarde = 0
boa_noite = 0
while i < x:
    bom_dia += 1
    j = 0
    while j < y:
        boa_tarde += 1
        j += 1
    i += 1

boa_noite +=1

print(bom_dia, boa_tarde, boa_noite)
