import sys
sys.stdin = open('input.txt')

def calculate(form):
    stack = []

    for char in form:
        if char.isdigit():                      # 숫자일 경우
            stack.append(int(char))               # 바로 stack에 push
        else:
            if char == '.':                     # .일 경우
                if len(stack) == 1:               # stack에 값이 하나만 있을 때
                    return stack.pop()            # 결과값 반환
                else:                             # stack에 값이 하나가 아닐 떄
                    return 'error'                # 'ERROR'
            else:                               # 연산자일 경우
                if len(stack) < 2:                # 연산에 필요한 숫자가 2개 미만일 때
                    return 'error'                # 'ERROR'
                else:                             # 연산에 필요한 숫자가 2개 이상일 때
                    x = stack.pop()               # 2개의 숫자를 pop하고
                    y = stack.pop()
                    if char == '+':               # 연산을 진행한 뒤, 결과값을 stack에 push
                        stack.append(y + x)
                    elif char == '-':
                        stack.append(y - x)
                    elif char == '*':
                        stack.append(y * x)
                    elif char == '/':
                        stack.append(y // x)

T = int(input())

for test_case in range(1, T+1):
    formula = list(map(str, input().split()))

    print('#{} {}'.format(test_case, calculate(formula)))