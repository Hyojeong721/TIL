import sys
sys.stdin = open('input.txt')

expr = list(input())

stack = []
for i in expr:
    if i not in '0123456789':
        stack.append(i)
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            stack.append(i)
        elif i == '+' or i == '-':
            stack.append(i)

            # 미완성

