import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    chars = input()
    stack = []

    for i in range(len(chars)):
        if not stack or stack[-1] != chars[i]:
            stack.append(chars[i])
        else:
            stack.pop()

    print('#{} {}'.format(tc, len(stack)))
