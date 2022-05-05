# a = 3
# b = 4
# c = 5
# print(a+b%c<c//a*b or not b**2<a*b+2 and c+a/b>=a+b//a*c+1)

n1 = 10
n2 = 5

if n1%11 == 1:
    if n1%2 == 1:
        n1 = n2+10
    else:
        n2 = n1+10.5
else:
    n1 = n1%11
    if n1%2 == 0 and n1%2 ==1:
        n2 = n1 + 5
n2 = n2//2+5*n2//3
print(n1+n2%2)
print(n1+n2)
