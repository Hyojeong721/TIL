import sys
sys.stdin = open('input.txt')

calculation = input()
stack = []
operator = ['+', '-', '*', '/', '(', ')']
isp = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 3,
}

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
        while stack != [] and isp[stack[-1]] > isp[char]:
            output += stack.pop()
        stack.append(char)

while stack:
    output += stack.pop()


print(output)

