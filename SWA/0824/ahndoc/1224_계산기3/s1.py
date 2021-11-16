import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    P = input()
    stack = []
    postfix = []
    for i in P:g
        if i.isdigit():
            postfix.append(i)
            continue

        if i == ')':
            temp = ''
            for j in stack:
                temp += j
            N = temp.rfind('(') + 1
            for k in range(len(stack), N, -1):
                postfix.append(stack.pop())
            stack.pop()
        elif i == '(':
            stack.append(i)

        elif i == '*':
            if stack and stack[-1] == '*':
                while stack and stack[-1] == '*':
                    postfix.append(stack.pop())
                stack.append('*')
            elif stack and stack[-1] == '+':
                stack.append('*')
            elif stack and stack[-1] == '(':
                stack.append('*')

        elif i == '+':
            if stack and (stack[-1] == '*' or stack[-1] == '+'):
                while stack and (stack[-1] == '*' or stack[-1] == '+'):
                    postfix.append(stack.pop())
                stack.append('+')
            elif stack and stack[-1] == '(':
                stack.append('+')

    result = []
    for i in postfix:
        if i in '0123456789':
            result.append(int(i))
        elif i == '*':
            num2 = result.pop()
            num1 = result.pop()
            result.append(num1 * num2)
        elif i == '+':
            num2 = result.pop()
            num1 = result.pop()
            result.append(num1 + num2)

    print('#{} {}'.format(tc, *result))
