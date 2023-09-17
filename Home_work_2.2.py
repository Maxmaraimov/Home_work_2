from math import sqrt
s = int(input())
p = int(input())
d = s**2 - 4*p
if d > 0:
    x = (1/2) * (s+sqrt(d))
    y = (1/2) * (s-sqrt(d))
    print(round(x,2), round(y, 2))
else:
    print('Vvedete drugoy chislo!')