import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    answer = []
    code = list(input().split())
    stack = []
    for c in code:
        if c == '+':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                c = a + b
                stack.append(c)
            else:
                answer.append('error')
                break

        elif c == '-':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                c = a - b
                stack.append(c)
            else:
                answer.append('error')
                break

        elif c == '*':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                c = a * b
                stack.append(c)
            else:
                answer.append('error')
                break

        elif c == '/':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                c = a // b
                stack.append(c)
            else:
                answer.append('error')
                break

        elif c == '.':
            if len(stack):
                answer.append(stack.pop())
            else:
                answer.append('error')
        else:
            stack.append(c)

    if len(stack):
        answer.append('error')

    print('#{} {}'.format(TC, answer.pop()))