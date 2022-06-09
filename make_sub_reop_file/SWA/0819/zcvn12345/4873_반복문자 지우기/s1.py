import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    s = list(input())
    stack = []
    for i in range(len(s)):
        if len(stack) != 0 and s[i] == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(s[i])

    print('#{0} {1}'.format(tc, len(stack)))
