import sys
sys.stdin = open("input.txt")


def infix_to_postfix(sentence):
    """
    주어진 계산식을 후위 표기식으로 변환한다.
    Args:
        sentence: 중위 표기식으로 쓰인 계산식 (문자열)
    Returns:
        postfix: 계산식의 후위 표기식 (문자열)
    """
    # isp: 스택에서 뺄 때의 우선순위
    isp = {'*': 2, '+': 1, '(': 0}
    # icp: 스택에 넣을 때의 우선순위
    icp = {'*': 2, '+': 1, '(': 3}

    stack = []
    postfix = ''

    for char in sentence:
        # 현재 탐색중인 문자가 ')'라면
        if char == ')':
            # 여는 괄호가 나올 때까지 스택에서 빼서 postfix에 붙인다.
            while stack[-1] != '(':
                postfix += stack.pop()
            # 여는 괄호도 스택에서 뺀다.
            stack.pop()
        # 현재 탐색중인 문자가 숫자(피연산자)라면
        elif '0' <= char <= '9':
            # 바로 postfix에 붙인다.
            postfix += char
        # 현재 탐색중인 문자가 '(', '+', '*' 중 하나라면
        else:
            # 스택이 비거나
            # 현재 탐색중인 문자의 우선순위가 스택의 마지막 값 우선순위보다 높아질 때까지
            while stack and isp[stack[-1]] >= icp[char]:
                postfix += stack.pop()
            # 현재 탐색중인 문자를 stack에 넣는다.
            stack.append(char)

    # 스택에 남은 문자를 하나씩 빼서 postfix에 붙인다.
    while stack:
        postfix += stack.pop()

    return postfix


def calculate_postfix(postfix):
    """
    후위 표시식의 계산 결과를 구한다.
    Args:
        postfix: 후위 표기식으로 쓰인 계산식 (문자열)
    Returns:
        계산식의 결과값 (정수)
    """
    stack = []

    for char in postfix:
        # 현재 탐색중인 문자가 '+'라면
        if char == '+':
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        # 현재 탐색중인 문자가 '*'라면
        elif char == '*':
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        # 현재 탐색중인 문자가 숫자(피연산자)라면
        else:
            stack.append(int(char))

    return stack[0]


T = 10

for tc in range(1, T + 1):
    N = int(input())
    sentence = input()

    result = calculate_postfix(infix_to_postfix(sentence))
    print("#{} {}".format(tc, result))
