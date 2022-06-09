'''

나눗셈 연산에서, int 로 변환 안 하면 소숫점 나와서(?) 채점케이스가 몇개 안됐다.
그래서 if 문을 계속 바르면서 error가 될 수 있는 조건을 추가했기 떄문에 코드가 더 더러워졌다.
내 시간~~~

'''

import sys
sys.stdin = open('input.txt')


operator = ['*', '/', '+', '-']

def calculate_postfix(string):
    global operator
    stack = []

    for idx, token in enumerate(string):
        # 1. 연산자인 경우
        if token in operator:
            # stack 내에 2개 미만 있으면 error
            if len(stack) < 2:
                return 'error'
            # stack 내에 2개 이상 있으면 연산 진행
            t2 = stack.pop()
            t1 = stack.pop()
            if token == '*':
                stack.append(t1 * t2)
            elif token == '/':
                # 나누어 떨어지지 않으면 error
                if t1 % t2 or not t2:
                    return 'error'
                stack.append(int(t1 / t2))      # 이거 int로 변환 안 하면 나눗셈해도 소숫점 생김;;;;;;ㅠㅠ내시간..
            elif token == '+':
                stack.append(t1 + t2)
            else:
                stack.append(t1 - t2)
        # 2. . 인 경우
        elif token == '.':
            # stack 에 1개 있고, 문장의 마지막이면 결과값 반환
            if len(stack) == 1 and idx == len(string) - 1:
                return stack.pop()
            else:
                return 'error'
        # 3. 피연산자인 경우
        elif token.isdigit():
            stack.append(int(token))
        # 4. 모두 아니면 error
        else:
            return 'error'

    # 끝났는데 return 안했으면 error
    return 'error'


T = int(input())
for tc in range(1, T + 1):
    string = input().split()
    result = calculate_postfix(string)
    print('#{} {}'.format(tc, result))