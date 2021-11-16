T = int(input())
start = ['(', '{']
end = [')', '}']

for t in range(1, T+1):
    code = input().strip()
    stack = []

    for c in code:
        if c in start:
            stack.append(c)

        elif c in end:
            if len(stack) == 0:
                stack.append('error')
                break

            elif stack[-1] == '(':
                if c == ')': stack.pop()
                else:
                    stack.append('error')
                    break

            elif stack[-1] == '{':
                if c == '}': stack.pop()
                else:
                    stack.append('error')
                    break

        # print('c:', c, ' stack:', stack)


    result = 1
    if len(stack) > 0:
        result = 0
    print('#{} {}'.format(t, result))