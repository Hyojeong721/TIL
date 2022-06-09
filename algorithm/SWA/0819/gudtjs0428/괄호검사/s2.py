import sys
sys.stdin = open('input.txt')

def check_brackets(string):
    brackets = ''
    for char in string:
        if char == '(' or char == ')' or char == '{' or char == '}':
            brackets += char

    if len(brackets) % 2:
        return 0

    i = 0
    while i < len(brackets) - 1:
        if brackets[i] == '(':
            if brackets[i+1] == '{' or brackets[i+1] == '(':        # {}{}{}
                i += 1
            elif brackets[i+1] == ')':
                brackets = brackets[:i] + brackets[i+2:]
                i = 0
            else:
                return 0
        elif brackets[i] == '{':
            if brackets[i+1] == '(' or brackets[i+1] == '{':
                i += 1
            elif brackets[i+1] == '}':
                brackets = brackets[:i] + brackets[i + 2:]
                i = 0
            else:
                return 0
    if brackets:
        return 0
    return 1

       # if brackets[i] == ')':
       #     if brackets[i-1] == '{':
       #         return 0
       #     elif brackets[i-1] == '}':
       #         while


T = int(input())
for tc in range(1, T + 1):
    string = input()
    print('#{} {}'.format(tc, check_brackets(string)))