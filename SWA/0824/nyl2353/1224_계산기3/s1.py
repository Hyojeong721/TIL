import sys
sys.stdin = open('input.txt')


def infix_to_postfix(string):
    """
    중위 표기식을 후위 표기식으로 변환

    :param string: 중위 표기된 문자열
    :return: 후위 표기된 문자열
    """
    stack = []
    top = -1
    postfix = ''

    # isp: in-stack priority, icp: in-coming priority
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    operand = [str(i) for i in range(10)]

    for token in string:
        # 1. operator 면, <- ')' 제외
        if token in icp:
            # 스택이 비어있거나, isp 보다 icp 가 크면 push
            if top == -1 or isp[stack[top]] < icp[token]:
                stack.append(token)
                top += 1
            # isp 보다 icp 가 작으면 pull
            elif isp[stack[top]] >= icp[token]:
                while True:
                    if top >= 0 and isp[stack[top]] >= icp[token]:
                        popped = stack.pop()
                        top -= 1
                        postfix += popped
                    else:
                        stack.append(token)
                        top += 1
                        break

        # 2. operator 중 ')' 면,
        elif token == ')':
            while True:
                popped = stack.pop()
                top -= 1
                if popped == '(':
                    break
                else:
                    postfix += popped

        # 3. operand 면,
        elif token in operand:
            postfix += token

    # stack 에 남아있는 연산자를 모두 pop
    while stack:
        postfix += stack.pop()

    return postfix


def calculate_postfix(string):
    """
    후위 표기된 문자열 수식을 계산한다.

    :param string: 후위 표기된 문자열
    :return: 수식 결과
    """
    operand = [str(i) for i in range(10)]
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


for tc in range(1, 11):
    N = int(input())
    string = input()
    postfix = infix_to_postfix(string)
    result = calculate_postfix(postfix)
    print('#{} {}'.format(tc, result))