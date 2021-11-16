import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    expr = list(input().split())

    stack = []
    check = 0

    for i in expr[0:-1]:
        if i.isdigit():
            stack.append(i)
        else:
            try:
                if i == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif i == '-':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b-a))
                elif i == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif i == '/':
                    a = int(stack.pop())
                    b = int(stack.pop())
                    stack.append(int(b//a))
            except:
                check = -1

    if check != 0 or len(stack) != 1:
        print('#{} {}'.format(tc, 'error'))
    else:
        print('#{} {}'.format(tc, stack[0]))