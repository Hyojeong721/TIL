import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = list(input())
    stack1 = []  # 숫자
    stack2 = []  # 부호
    result = 0

    for i in arr:
        if i not in '+*':
            stack1.append(i)
        else:
            stack2.append(i)

    while len(stack2):
        s = stack2.pop()
        if s == '*':
            a = stack1.pop()
            b = stack1.pop()
            c = int(a)*int(b)
            stack1.append(c)
        else:
            temp = stack1.pop()
            result += int(temp)
    print('#{} {}'.format(tc, result + int(stack1[0])))
