import sys
sys.stdin = open('input.txt')

def if_brackets_closed_right(string):
    stack = []
    for i in range(len(string)):
        if not stack and string[i] == ')':
            return 0
        elif not stack and string[i] == '}':
            return 0
        elif string[i] == '(' or string[i] == '{':
            stack.append(string[i])
        elif string[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            elif stack[-1] == '{':
                return 0
        elif string[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            elif stack[-1] == '}':
                return 0

    if stack:
        return 0
    return 1


T = int(input())
for test_case in range(1, T + 1):
    string = input()
    print('#{} {}'.format(test_case, if_brackets_closed_right(string)))