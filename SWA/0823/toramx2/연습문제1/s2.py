import sys
sys.stdin = open('input.txt')

def icp(x):
    if x == '+' or x == '-':
        return 1
    elif x == '*' or x == '/':
        return 2
    elif x == '(':
        return 3

def isp(x):
    if x == '+' or x == '-':
        return 1
    elif x == '*' or x == '/':
        return 2
    elif x == '(':
        return 0


infix = list(input().split())
postfix = []
stack = []
top = ''
num = '0123456789'

for a in infix:
    if a in num:
        postfix.append(a)
    else:
        if a == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                postfix.append(x)
        elif a == '(':
            stack.append(a)
            top = stack[-1]
        else:
            while len(stack) > 0:
                top = stack[-1]
                if icp(a) > isp(top):
                    break
                postfix.append(stack.pop())
            stack.append(a)


for i in range(len(stack)-1, -1, -1):
    postfix.append(stack[i])

print(*postfix)