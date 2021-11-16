import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    C = input()
    stack = []
    result = 1
    for i in C:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                result = 0
            else:
                stack.pop(-1)
        elif i == '}':
            if len(stack) == 0 or stack[-1] != '{':
                result = 0
            else:
                stack.pop(-1)

    if len(stack) != 0:
        result = 0

    print('#{0} {1}'.format(tc, result))


