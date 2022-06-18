T = 1

for TC in range(1, T+1):
    answer = 0
    N = 9
    input_str = '3+4+5*6+7'
    stack = []
    result_str = []
    for c in input_str:
        if c in '+*':
            if not len(stack):
                stack.append(c)
            else:
                # 읽어들인 입력이 스택의 top 보다 우선순위가 낮거나 같은 경우
                if c == '+' or (c == '*' and stack[-1] == '*'):
                    result_str.append(stack.pop())
                    stack.append(c)
                # 우선순위가 더 높을 경우 push
                else:
                    stack.append(c)
        else:
            result_str.append(c)

    while len(stack):
        result_str.append(stack.pop())

    print(str(result_str))
    print('#{} {}'.format(TC, answer))
