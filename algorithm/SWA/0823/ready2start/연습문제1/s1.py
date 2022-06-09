import sys
sys.stdin = open("input.txt")


def infix_to_postfix(infix):
    """
    중위표기법으로 작성된 수식문자열을 후위표기법으로 변환한다.
    Args:
        infix: 중위표기법으로 작성된 수식 (문자열)
    Returns:
        postfix: 후위표기법으로 작성된 수식 (문자열)
    """
    # in-stack priority dictionary
    isp_dict = {
        '*': 2, '/': 2, '+': 1, '-': 1, '(': 0
    }

    # in-coming priority dictionary
    icp_dict = {
        '*': 2, '/': 2, '+': 1, '-': 1, '(': 3
    }

    postfix = ''
    stack = []

    for char in infix:
        if '0' < char < '9':
            postfix += char
        elif char == ')':
            # 왼쪽 괄호가 나올 때까지 스택에서 하나씩 빼서 더한다.
            while stack[-1] != '(':
                postfix += stack.pop()
            # 왼쪽 괄호가 나오면 스택에서 빼기만 한다.
            stack.pop()
        else:
            while stack and icp_dict[char] <= isp_dict[stack[0]]:
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    return postfix


infix = input()
postfix = infix_to_postfix(infix)
print(postfix)
