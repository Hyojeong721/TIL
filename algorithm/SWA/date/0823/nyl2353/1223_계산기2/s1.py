import sys
sys.stdin = open('input.txt')


operator = ['*', '+']
operand = [str(i) for i in range(10)]

def to_postfix(string):
    """
    덧셈, 곱셈 연산의 중위 표기법을 후위 표기법으로 바꾼다.

    :param string: 중위 표기법의 문자열 수식
    :return: 후위 표기법의 문자열 수식
    """
    global operand
    stack = []
    postfix = ''

    for token in string:
        # operand 인 경우
        if token in operand:
            postfix += token

        # * 이면 push
        elif token == '*':
            stack.append(token)

        # + 이면 모두 pop 한 뒤에, push
        elif token == '+':
            while stack:
                postfix += stack.pop()
            stack.append(token)

    # stack 에 남아있는 연산자(+) pop
    while stack:
        popped = stack.pop()
        postfix += popped

    return postfix


def calculate_postfix(string):
    """
    후위 표기법의 문자열 수식을 계산한다.

    :param string: 후위 표기법의 문자열 수식
    :return: 수식 결과
    """
    global operand
    stack = []

    for token in string:
        if token in operand:
            stack.append(token)
        else:
            t2 = int(stack.pop())
            t1 = int(stack.pop())
            if token == '+':
                stack.append(t1 + t2)
            elif token == '*':
                stack.append(t1 * t2)

    return stack.pop()


# 10개 test case에 대해 진행
for tc in range(1, 11):
    N = int(input())
    string = input()
    postfix = to_postfix(string)
    result = calculate_postfix(postfix)
    print('#{} {}'.format(tc, result))