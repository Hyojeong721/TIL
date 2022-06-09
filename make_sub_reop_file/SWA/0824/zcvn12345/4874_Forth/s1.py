import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    board = list(input().split())
    stack = []
    result = ''
    for i in board:
        if i == '.':
            if len(stack) != 1:
                result = 'error'
            else:
                result = stack[0]

        else:
            if i.isdecimal():
                stack.append(i)
            else:
                if len(stack) < 2:
                    result = 'error'
                    break
                else:
                    A = int(stack.pop())
                    B = int(stack.pop())

                    if i == '+':
                        stack.append(B+A)
                    elif i == '-':
                        stack.append(B-A)
                    elif i == '*':
                        stack.append(B*A)
                    elif i == '/':
                        stack.append(B//A)

    print(f'#{tc} {result}')
