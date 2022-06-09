a = 4
b = 5

if a > b:
    A = True
    B = False
else:
    A = False
    B = True

if a >= b:
    C = True
    D = False
else:
    C = False
    D = True

print(a, '>', b, '---', bool(a>b))
print(a, '<', b, '---', B)
print(a, '>=', b, '---', C)
print(a, '<=', b, '---', D)

print('hi', 'hello', sep='7')
