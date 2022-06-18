import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    nums = input()
    postfix = ''
    stack = []
    for i in nums:
        if i.isdecimal():
            postfix += i
        elif len(stack) == 0:
            stack.append(i)
        elif i == '+':
                postfix += stack.pop()
                stack.append(i)
        elif i == '*':
            if stack[-1] == '+':
                stack.append(i)
            else:
                postfix += stack.pop()
                stack.append(i)
    for i in range(len(stack)):
        postfix += stack.pop()

    stack = []
    for i in postfix:
        if i.isdecimal():
            stack.append(i)
        else:
            if i == '+':
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                c3 = c2 + c1
                stack.append(c3)
            else:
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                c3 = c2 * c1
                stack.append(c3)

    print('#{0} {1}'.format(tc, stack[0]))