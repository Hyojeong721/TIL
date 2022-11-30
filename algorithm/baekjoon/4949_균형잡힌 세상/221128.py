import sys
input = sys.stdin.readline

def checkout(k):
    global stack
    # stack이 비어있으면 아웃
    if not stack:
        return False
    else:
        t = stack.pop()

    if k == ')' and t != '(':
            return False
    elif k == ']' and t != '[':
            return False
    return True

while True:
    arr = list(input())
    res = 'yes'
    stack = []
    # 종료조건
    if len(arr) == 2 and arr[0] == '.':
        break
    # 문자열 순서대로 가봅니다.
    for k in arr:
        # 한줄 종료
        if k == '.':
            break
        # 여는 괄호 있으면 stack에 넣어요
        if k in ('(', '['):
            stack.append(k)
        # 닫는 괄호 나오면 checkout 검사를 시작합니다.
        elif k in (')', ']'):
            # false결과값인 경우 res는 no로 확정
            if not checkout(k):
                res = 'no'
                break
    # 검사다했는데 stack에 아직 남아있는 경우, no야
    if stack:
        res = 'no'

    print(res)

