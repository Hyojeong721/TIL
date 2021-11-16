import sys
sys.stdin = open("input.txt")

#######중위 표기법에서 후위 표기법으로 변환한다.
# 모든 연산자그룹에 우선순위대로 괄호를 배치한다.
# (2+((3*4)/5))

# 각 괄호 세트에서, 연산자를 닫힌 괄호 바로 앞으로 옮긴다.
# (2((34*)5/)+)

# 모든 괄호를 제거한다.
# 234*5/+
########################################
# 1. 피 연산자는 우측으로 옮기고 2. 연산자는 스택에 넣는다.


# 연산자 : +, *
# 피연산자 : 0부터 9까지의 정수


# 우선순위 정보를 저장할 딕셔너리
priority = {
    '*' : 3,
    '/' : 3,
    '+' : 2,
    '-' : 2,
    '(' : 1
}

# 피연산자는 우측으로 옮기고, 연산자는 스택에 넣는다.
# 피연산자를 다 옮기면 스택 내의 연산자를 pop 하여 옮긴다.

# 만약 넣으려는 연산자보다 스택 내 연산자의 우선순위가 높거나 같다면 해당 연산자를 뽑아서
# 우측에 옮긴 후 연산자를 스택에 넣는다.

# 여는 괄호는 무조건 스택에 넣는다. 이후 닿는 괄호를 만나게 되면 여는 괄호를 만날때까지
# 스택에서 연산자를 뽑아오고 두 괄호를 모두 삭제한다.

T = int(input())

for tc in range(1, T+1):
    num = int(input())
    # 중위표현식과 후위표현식을 저장할 리스트
    expr = []
    # 연산자를 저장할 스택
    operator = []  # stack
    result = []

    tmp = input()

    # 식을 입력할 때, 띄어쓰기를 없애 임시변수에 저장 후 expr에 저장
    for i in tmp:
        if i == ' ':
            continue
        expr.append(i)


    for i in expr:
        # 열린 괄호는 무조건 스택에 집어넣는다.
        if i == '(':
            operator.append(i)

        elif i in '+*':
            # 연산자는 스택이 비어있으면 넣고
            if len(operator) == 0:
                operator.append(i)
            # 비어있지 않다면 스택의 가장 위에 있는 연산자의 우선순위 비
            else:
                # 스택 내 연산자의 우선순위가 높거나 같다면 해당 연산자를 뽑아 결과 리스트에 넘기고 스택에 집어넣는
                if priority[operator[-1]] >= priority[i]:
                    result.append(operator.pop())
                    operator.append(i)
                else:
                    operator.append(i)
        # 닫는 괄호를 만나면 스택 안에 여는 괄호를 만날때까지 연산자 뽑아 결과
        elif i == ')':
            while True:
                tmp = operator.pop()
                if tmp == '(':
                    break
                result.append(tmp)
        # 토큰이 피연산자면 바로 결과
        else:
            result.append(i)
    # 다 넘겼다면 스택에 있는 나머지 연산자를 모두 결과리스트에 넘
    while not(len(operator) == 0):
        result.append(operator.pop())

    result = ''.join(result)


    print('#{} {}'.format(tc, result))