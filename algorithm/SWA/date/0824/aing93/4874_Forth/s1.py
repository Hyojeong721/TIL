import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    Data = list(input().split())
    N = len(Data)
    stack = []
    flag = 0

    for i in range(N-1):
        if Data[i].isdigit():
            stack.append(Data[i])
        else:
            try:
                num2, num1 = int(stack.pop()), int(stack.pop())
                if Data[i] == "+":
                    result = num1 + num2
                elif Data[i] == "-":
                    result = num1 - num2
                elif Data[i] == "/":
                    result = num1 // num2
                elif Data[i] == "*":
                    result = num1 * num2

                stack.append(result)
            except:
                flag = 'error'

    if flag == 0 and len(stack) == 1:
        print('#{} {}'.format(tc, stack[0]))
    elif flag == 'error' or len(stack) > 1:
        print('#{} error'.format(tc))


