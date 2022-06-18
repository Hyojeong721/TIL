import sys
sys.stdin = open("input.txt")


def postfix(sentence):
    """
    계산식을 인자로 받아, 후위 표기식을 구한다.
    (단, 계산식의 연산자는 +, * 두 종류이다.)

    Args:
        sentence: 계산식 (문자열)
    Returns:
        result: 계산식의 후위 표기식
    """
    stack = []
    result = ""

    for char in sentence:
        # 현재 문자가 '+' 연산자라면
        if char == '+':
            while stack:
                result += stack.pop()
            stack.append(char)
        # 현재 문자가 '+' 연산자라면
        elif char == '*':
            while stack and stack[-1] == '*':
                result += stack.pop()
            stack.append(char)
        # 현재 문자가 피연산자라면
        else:
            result += char

    while stack:
        result += stack.pop()

    return result


def calculate_postfix(postfix_exp):
    """
    후위 표기식을 인자로 받아, 계산식의 결과를 구한다.
    (단, 계산식의 연산자는 +, * 두 종류이다.)

    Args:
        postfix_exp: 후위 표기식 (문자열)
    Returns:
        result: 계산식의 결과값 (숫자)
    """
    stack = []

    for char in postfix_exp:
        # 현재 문자가 '+' 연산자라면
        if char == '+':
            num1, num2 = stack.pop(), stack.pop()
            stack.append(int(num1) + int(num2))
        # 현재 문자가 '*' 연산자라면
        elif char == '*':
            num1, num2 = stack.pop(), stack.pop()
            stack.append(int(num1) * int(num2))
        # 현재 문자가 피연산자라면
        else:
            stack.append(char)

    return stack[0]


T = 10

for tc in range(1, T + 1):
    n = int(input())
    sentence = input()

    postfix_exp = postfix(sentence)
    print("#{} {}".format(tc, calculate_postfix(postfix_exp)))
