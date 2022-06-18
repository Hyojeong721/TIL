import sys
sys.stdin = open('input.txt')


def calculator(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2


for tc in range(1, 11):
    N = int(input())
    tree = ['0'] * (N + 1)
    check_op = [False] * (N + 1)
    child = [[0, 0]] * (N + 1)
    for _ in range(N):
        idx, *v = input().split()
        tree[int(idx)] = v[0]
        if len(v) > 1:
            check_op[int(idx)] = True
            child[int(idx)] = [int(v[1]), int(v[2])]

    for i in range(N, 0, -1):
        if check_op[i]:
            operator = tree[i]
            num1, num2 = int(tree[child[i][0]]), int(tree[child[i][1]])
            tree[i] = calculator(operator, num1, num2)

    print('#{} {}'.format(tc, int(tree[1])))