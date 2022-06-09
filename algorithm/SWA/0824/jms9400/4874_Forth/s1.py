import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = list(input().split())

    stack = []

    for i in arr:
        if i not in '+*/-.':
            stack.append(int(i))
        else:
            if i == '.':
                if len(stack) > 1:
                    print('#{} error'.format(tc))
                    break
                else:
                    print('#{} {}'.format(tc, stack[0]))
                    break
            elif len(stack) < 2:
                print('#{} error'.format(tc))
                break
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
            else:
                stack.append(a - b)
