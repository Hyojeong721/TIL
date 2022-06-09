import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    chrs = input()
    stack = []
    result = 1

    for chr in chrs:
        if chr == '{' or chr == '(':
            stack.append(chr)

        elif chr == '}':
            if len(stack) == 0 or stack[-1] != '{':
                result = 0
                break
            else:
                stack.pop()

        elif chr == ')':
            if len(stack) == 0 or stack[-1] != '(':
                result = 0
                break
            else:
                stack.pop()

    if len(stack):
        result = 0

    print('#{} {}'.format(tc, result))