import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    test = input()
    lst = []
    for t in test:  # 괄호만 남긴 리스트를 만듭니다.
        if t in ('{}()'):
            lst.append(t)

    stack = []
    result = 1
    for i in lst: # 예람님 풀이처럼 딕셔너리 쓰면 편할 듯
        if len(stack): # stack이 비어있지 않을 때
            if i == ')':
                if not stack[-1] == '(':
                    result = 0
                    break
                else:
                    stack.pop()
            elif i == '}':
                if not stack[-1] == '{':
                    result = 0
                    break
                else:
                    stack.pop()
            else:
                stack.append(i)

        else: # 스택이 비어있을 때는 그냥 해당 원소를 append합니다.
            stack.append(i)

    if len(stack) != 0: # 지워지지 않은 괄호가 있다면 0을 출력합니다.
        result = 0
    print('#{} {}'.format(tc, result))