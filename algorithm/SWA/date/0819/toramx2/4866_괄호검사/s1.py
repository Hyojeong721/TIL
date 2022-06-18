import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    text = list(input())
    stack = []

    for char in text:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                stack.append('StackUnderflow')
                break
            elif stack.pop() != '(':
                break
        elif char == '}':
            if len(stack) == 0:
                stack.append('StackUnderflow')
                break
            elif stack.pop() != '{':
                break

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print('#{0} {1}'.format(test_case, result))