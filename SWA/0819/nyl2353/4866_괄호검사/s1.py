import sys
sys.stdin = open('input.txt')


def check_bracket(text):
    """
    괄호가 제대로 짝을 이뤘으면 1, 아니면 0을 반환하는 함수
    :param text: 검사할 문자열
    :return: boolean
    """
    stack = []
    pairs = {'(': ')', '{': '}'}

    for char in text:
        # char 가 ( 또는 { 이면, stack 에 push
        if char in pairs:
            stack.append(char)

        # char 가 ) 또는 } 이면,
        elif char in pairs.values():
            # stack 이 차있을 때, pop(왼쪽 괄호)이 char(오른쪽 괄호)과 다르면 0 반환
            if len(stack):
                check = stack.pop()
                if char != pairs[check]:
                    return 0
            # stack 이 비어있다면 0 반환
            else:
                return 0

    # 모든 문자열을 검사 한 후, stack 이 차있으면 0 반환
    if len(stack):
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    text = input()
    result = check_bracket(text)
    print('#{0} {1}'.format(tc, result))