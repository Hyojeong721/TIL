import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1 + T):

    command = input()

    stack = []
    target = ['(', ')', '{', '}']
    for char in command:
        if char in target:
            stack.append(char)
            if len(stack) >= 2 and (stack[-2] + stack[-1] == '()' or stack[-2] + stack[-1] == '{}'):
                stack.pop()
                stack.pop()

    if stack:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))