import sys
sys.stdin = open('input.txt')

for tc in range(2):
    arr = ' ' + input() + ' '

    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ' ': -1}
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ' ': -1}

    stack = []
    result = ''

    for i in range(len(arr)):
        # 문자가 연산자인 경우
        if arr[i] in isp.keys():
            # 새로 들어오는 문자의 값을 지정
            icp_number = icp.get(arr[i])
            # stack에 문자가 있는 경우 top 지정 / 없으면 top = 0
            if stack:
                top_number = isp.get(stack[-1])
            else:
                top_number = 0
            # 새 문자와 top 문자의 크기를 비교해서 새문자값이 큰 경우에만 stack에 push -> top은 새로 들어온 문자로 변경
            if icp_number > top_number:
                stack.append(arr[i])
                top = stack[-1]
            # 새 문자값이 top 값보다 작거나 동일한 경우
            else:
                # stack에 문자가 들어있고 / 새로 들어오는 문자보다 값이 작아질때까지 출력!
                while icp_number <= top_number and stack:
                    if stack:
                        result += stack.pop()
                        # 하나 빠지면 top을 stack의 마지막 값으로 변경
                        if stack:
                            top_number = isp.get(stack[-1])
                # top 값이 새로들어오는 문자 값보다 작아졌을 때 새 문자를 stack에 push
                stack.append(arr[i])
        # 문자가 ')'일 경우
        elif arr[i] ==')':
            a = stack.pop()
            # '('을 만날 때까지 stack에서 계속 출력
            while a != '(':
                result += a
                if stack:
                    a = stack.pop()
                    # 만약 stack이 빈 경우 종료
                    if a == ' ':
                        break
        # 문자가 숫자인 경우
        else:
            result += arr[i]

    print(result)
