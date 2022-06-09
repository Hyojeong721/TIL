import sys
sys.stdin = open("input.txt")
# 테스트 케이스를 받아온다.
T = int(input())
for tc in range(1, T+1):
    string_check = input()
    # stack 초기화
    stack = []
    for i in string_check:
            # 비교하기 위해 (, {, [ 열리는 기호있으면 stack 에 더한다.
        if i == "(" or i == "[" or i == "{":
            stack.append(i)
            # stack에 pop한 후 쌍을 비교한다. 이후, 짝이 맞지 않거나 비어있는데 pop 하면 0
        elif i == ")" or i == "]" or i == "}":
            if len(stack) != 0:
                tmp = stack.pop()
                if i == ')' and tmp != '(':
                    result = 0
                    break
                if i == ']' and tmp != '[':
                    result = 0
                    break
                if i == '}' and tmp != '{':
                    result = 0
                    break
            else:
                result = 0
                break
    # stack 이 남아있다면 아니기에, 없을 때 1 반환, 즉 stack 의 길이가 0이면 짝이 잘 맞았다는 뜻

    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc, result))