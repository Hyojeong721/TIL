import sys
sys.stdin = open('input.txt')

def check(c):
    if c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = input()
    stack = []
    postfix = []

    # 중위표기법 수식을 후위표기법 수식으로 변환
    for i in data:
        if i in '0123456789':
            postfix.append(i)
        elif i == '+':
            if not stack:
                stack.append(i)
            elif check(i) > check(stack[-1]):
                stack.append(i)
            else:
                while stack and check(i) <= check(stack[-1]):
                    postfix.append(stack.pop())
                if not stack or check(i) > check(stack[-1]):
                    stack.append(i)
        elif i == '*':
            if not stack:
                stack.append(i)
            elif check(i) > check(stack[-1]):
                stack.append(i)
            else:
                while stack and check(i) <= check(stack[-1]):
                    postfix.append(stack.pop())
                if not stack or check(i) > check(stack[-1]):
                    stack.append(i)
    while stack:
        postfix.append(stack.pop())

    # 후위표기법 수식을 스택을 이용하여 계산
    for i in postfix:
        if i in '0123456789':
            stack.append(int(i))
        elif i == '+':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 + num2)

        elif i == '*':
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(num1 * num2)
    print('#{} {}'.format(tc, *stack))