import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    case = input()

    stack = []

    for i in range(len(case)):
        if case[i] == '(' or case[i] == '{':
            stack.append(case[i])
        elif case[i] == ')':
            if not stack or stack[-1] != '(':
                stack.append('F')
                break
            else:
                stack.pop()
        elif case[i] == '}':
            if not stack or stack[-1] != '{':
                stack.append('F')
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))







    # stack = ''
    # for i in case:
    #     if i == '{':
    #         stack += i
    #     elif i == '(':
    #         stack += i
    #     elif i == '}':
    #         stack += i
    #     elif i == ')':
    #         stack += i
    #
    # while '()' in stack or '{}' in stack:
    #     if '()' in stack:
    #         stack = stack.replace('()', '')
    #     elif '{}' in stack:
    #         stack = stack.replace('{}', '')
    #
    # if len(stack) == 0:
    #     print('#{} 1'.format(tc))
    # else:
    #     print('#{} 0'.format(tc))