import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(input())
    stack = []
    fomu = ''

    for c in arr:
        if c in '0123456789':
            fomu += c
        else:
            if c == ')':
                while len(stack):
                    s = stack.pop()
                    if s == '(':
                        break
                    else:
                        fomu += s
            elif c == '(':
                stack.append(c)
            else:
                if stack[-1] == '(':
                    stack.append(c)
                else:
                    if c == '+' and stack[-1] == '*':
                        s = stack.pop()
                        fomu += s
                    elif c == '*' and stack[-1] == '*':
                        s = stack.pop()
                        fomu += s
                    stack.append(c)

    stack2 = []
    for k in fomu:
        if k in '0123456789':
            stack2.append(int(k))
        else:
            b = stack2.pop()
            a = stack2.pop()
            if k == '+':
                stack2.append(a+b)
            else:
                stack2.append(a*b)
    print('#{} {}'.format(tc, stack2[0]))