import sys
sys.stdin = open('input.txt')

expr = input()
n = len(expr)
lst = []
for i in expr:
    if i.isdigit():
        print(i, end='')
    elif i in '+-/*':
        lst.append(i)

while lst:
    s = lst.pop()
    print(s, end='')