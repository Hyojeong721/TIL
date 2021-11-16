import sys
sys.stdin = open('input.txt')

T = 10
icp = {'*': 2, '+': 1, '(': 3}
isp = {'*': 2, '+': 1, '(': 0}
for tc in range(1, T + 1):
    length = int(input())
    stack = []
    ops = []
    lst = list(input())
    for i in lst:
        if i.isdigit():
            stack.append(i)


        else:
            if not len(ops):
                ops.append(i)

            else:
                if i == ')':
                    while ops[-1] != '(':
                        stack.append(ops.pop())
                    ops.pop()
                elif icp[i] > isp[ops[-1]]:
                    ops.append(i)

                else:
                    while True:
                        stack.append(ops.pop())
                        if (not len(ops)) or icp[i] > isp[ops[-1]]:
                            ops.append(i)
                            break

    while len(ops):
            stack.append(ops.pop())

    numbers = []
    result = []
    for j in stack:
        if j.isdigit():
            numbers.append(int(j))
        elif j == '*':
            b = numbers.pop()
            a = numbers.pop()
            numbers.append(a * b)

        elif j == '+':
            b = numbers.pop()
            a = numbers.pop()
            numbers.append(a + b)

    print('#{} {}'.format(tc, numbers[0]))


