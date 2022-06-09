import sys
sys.stdin = open("input.txt")


def operate(num1, num2, operator):
    """
    사칙연산의 계산 결과를 구한다.
    Args:
        num1, num2: 연산자 앞, 뒤의 피연산자 (정수)
        operator: 연산자 (+, -, *, /)
    Returns:
        연산의 계산 결과 (정수)
    """
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        # 정수를 반환해야 하므로 // 연산자를 대입한 값을 리턴한다.
        return num1 // num2


def calculate_postfix(codes):
    """
    후위 표기법으로 작성된 연산코드의 계산 결과를 구한다.
    Args:
        codes: 후위 표기법으로 작성된 계산식 (문자열)
               피연산자와 연산자는 여백으로 구분되며, 코드는 '.'으로 끝난다.
    Returns:
        연산 코드의 계산 결과 (정수)
        (단, 연산코드 형식이 잘못된 경우 'error')
    """
    stack = []

    for code in codes.split():
        # 현재 코드가 '.'인 경우
        if code == '.':
            # 스택에 남아있는 값이 하나라면 그 값을 리턴한다.
            if len(stack) == 1:
                return stack[0]
            # 스택이 비어있거나 값이 둘 이상 남아있다면 'error'를 리턴한다.
            else:
                return 'error'
        # 현재 코드가 숫자인 경우 => 스택에 넣는다.
        elif '0' <= code[0] <= '9':
            stack.append(int(code))
        # 현재 코드가 연산자인 경우
        else:
            # 스택에서 정수 2개를 꺼내서 연산한 결과를 다시 스택에 넣는다.
            try:
                # 주의) 첫번째 꺼낸 값이 연산자 뒤의 값이 되어야 한다.
                num2, num1 = stack.pop(), stack.pop()
                new_value = operate(num1, num2, code)
                stack.append(new_value)
            # 단, 스택에 있는 정수가 2개 미만이라면, 'error'를 리턴한다.
            except IndexError:
                return 'error'


T = int(input())

for tc in range(1, T + 1):
    codes = input()

    result = calculate_postfix(codes)
    print("#{} {}".format(tc, result))
