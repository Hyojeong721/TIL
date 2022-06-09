import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    lst = input().split()
    stack = []
    try:
        for i in lst:
            if i in '+/-*': # 사칙연산
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                else:
                    stack.append(a // b) # 항상 나누어 떨어지므로

            elif i.isdigit(): # 숫자라면
                stack.append(int(i))

            else:
                if len(stack) == 1:
                    print('#{} {}'.format(tc, stack.pop()))
                else:
                    print('#{} error'.format(tc))


    except: # 연산자가 너무 많아 스택이 비거나 해서 오류가 발생한다면
        print('#{} error'.format(tc))