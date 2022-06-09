import sys

sys.stdin = open('input.txt')

T = int(input())
operators = ['+', '-', '*', '/', '.']


def forth(text):

    stack = []

    for operator in operators:
        if operator in text:
            break
        else:
            return 'error'

    for idx, char in enumerate(text):
        if char.isdigit():
            stack.append(int(char))
        elif char == '.':
            if idx == len(text) - 1 and len(stack) == 1:
                return stack.pop()
            else:
                return 'error'
        else:
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                if char == '-':
                    stack.append(num1 - num2)
                if char == '*':
                    stack.append(num1 * num2)
                if char == '/':
                    stack.append(num1 // num2)
            else:
                return 'error'


for tc in range(1, T+1):
    calculation = input().split()
    result = forth(calculation)
    print(f'#{tc} {result}')