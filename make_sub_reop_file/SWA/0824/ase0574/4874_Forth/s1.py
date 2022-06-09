import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    arr = input().split()

    operator = ['+', '-', '*', '/']
    stack = []

    for i in range(len(arr)):
        # '.'이면
        if arr[i] == '.':
            # stack에 숫자가 1개인 경우
            if len(stack) == 1:
                print('#{} {}'.format(tc, stack.pop()))
            # 아닌 경우 error
            else:
                print('#{} error'.format(tc))


        # 연산자면
        elif arr[i] in operator:
            # stack에 2개 이상의 숫자가 들어있는 경우
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                # 연산자별 계산
                if arr[i] == '+':
                    stack.append(a + b)
                elif arr[i] == '-':
                    stack.append(a - b)
                elif arr[i] == '*':
                    stack.append(a * b)
                elif arr[i] == '/':
                    stack.append(a // b)


            # stack에 계산할 숫자가 없는 경우
            else:
                print('#{} error'.format(tc))
                break

        # 숫자면
        else:
            stack.append(arr[i])
