import sys
sys.stdin = open('input.txt')

operator = ['+', '-', '*', '/', '(', ')']
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,
}


def postfix(calculation):
    stack = []
    output = ''

    for char in calculation:
        if char not in operator:
            output += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack != [] and stack[-1] != '(':
                output += stack.pop()
                stack.pop()
        else:
            while stack != [] and isp[stack[-1]] >= isp[char]:
                output += stack.pop()
            stack.append(char)

    while stack:
        output += stack.pop()

    return output


def calculate(post_calculation):
    stack = []
    result = 0
    for char in post_calculation:
        if char not in operator:
            result

    return


T = 10

for tc in range(1, T+1):
    N = int(input())
    text = input()
    post_text = postfix(text)

