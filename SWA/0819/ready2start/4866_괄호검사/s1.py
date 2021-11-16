import sys
sys.stdin = open("input.txt")


def check_bracket(s):
    """인자로 받은 문자열의 괄호가 제대로 짝을 이루었는지 검사한다.

    Returns:
        문자열의 괄호가 짝을 잘 이루었다면 True, 아니면 False
    """
    stack = []

    for char in s:
        # 여는 괄호가 나온 경우
        if char == '(' or char == '{':
            # 스택에 추가시킨다.
            stack.append(char)
        # 닫는 괄호가 나온 경우
        elif char == ')' or char == '}':
            # 스택이 비어있다면 False를 반환한다.
            if not stack:
                return False
            # 스택이 비어있지 않다면 마지막으로 넣은 값을 뺀다.
            cnt = stack.pop()
            # 괄호의 짝이 맞는지 비교해서, 맞지 않으면 False를 반환한다.
            if (cnt == '(' and char != ')'
                    or cnt == '{' and char != '}'):
                return False

    # 순회를 마쳤는데 스택에 괄호가 남아있다면 False를 반환한다.
    if stack:
        return False
    # 스택에 괄호가 남아있지 않다면 True를 반환한다.
    return True


T = int(input())

for tc in range(1, T + 1):
    new_str = input()
    print("#{} {}".format(tc, int(check_bracket(new_str))))
