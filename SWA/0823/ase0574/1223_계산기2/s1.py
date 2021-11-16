import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = ' ' + input() + ' '

    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ' ': -1}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ' ': -1}

    stack = []
    result = ''

    # 후위 표기법으로 전환
    for i in range(len(arr)):
        if arr[i] in isp.keys():
            icp_number = icp.get(arr[i])
            if stack:
                top_number = isp.get(stack[-1])
            else:
                top_number = 0

            if icp_number > top_number:
                stack.append(arr[i])
                top = stack[-1]
            else:
                while icp_number <= top_number and stack:
                    if stack:
                        result += stack.pop()
                        if stack:
                            top_number = isp.get(stack[-1])
                stack.append(arr[i])

        elif arr[i] == ')':
            a = stack.pop()
            while a != '(':
                result += a
                if stack:
                    a = stack.pop()
                    if a == ' ':
                        break

        else:
            result += arr[i]

    result += ' '

    # 계산시작 stack = [' ']
    for i in range(len(result)):
        # 숫자이면 stack에 push
        if result[i] not in isp:
            stack.append(result[i])
        # 수식 끝난 경우
        elif result[i] == ' ':
            print("#{} {}".format(tc, stack[-1]))
            break
        # 연산자이면
        else:
            # 수식이 끝나지 않았다면
            if i != len(result)-1:
                # stack에서 피연산자 2개 pop
                b = int(stack.pop())
                a = int(stack.pop())
                # 연산자에 따라 계산
                if result[i] == '*':
                    ans = a * b
                else:
                    ans = a + b
                # 계산 결과 다시 stack에 push
                stack.append(ans)





