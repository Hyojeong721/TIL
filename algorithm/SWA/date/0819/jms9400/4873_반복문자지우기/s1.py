import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = list(input())
    s = str1.pop()
    stack = [0]
    stack.append(s)

    while len(str1):
        s = str1.pop()
        if stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    print('#{} {}'.format(tc, len(stack)-1))