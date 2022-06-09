import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    stick = input()
    n = len(stick)
    print(stick)

    stack = 0
    cnt = 0
    idx = 0
    while idx < n:
        if stick[idx] == '(' and stick[idx+1] == ')':
            idx += 2
            cnt += stack
        elif stick[idx] == '(':
            stack += 1
            idx += 1
        else:
            stack -= 1
            idx += 1
            cnt += 1

    print('#{} {}'.format(t, cnt))