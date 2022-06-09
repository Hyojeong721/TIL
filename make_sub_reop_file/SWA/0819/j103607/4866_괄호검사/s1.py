import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):

    sentence = input()

    stack = []
    for s in sentence:
        if s == '{' or s == '(':
            stack.append(s)

        if s == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            # 닫는 괄호가 더 많은 경우에도 짝이 안맞는 걸 알려면 일단 스택에 넣어야 됨
            else:
                stack.append(s)

        if s == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)

    if stack:
        result = 0
    else:
        result = 1


    print('#{} {}'.format(tc, result))