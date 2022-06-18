import sys
sys.stdin = open('input.txt')


def calc(x, c, y):
    x, y = int(x), int(y)

    if c == '+':
        return x + y
    elif c == '-':
        return x - y
    elif c == '*':
        return x * y
    elif c == '/':
        return x / y


T = 10
for tc in range(1, T+1):
    N = int(input())
    nodes = [0] + [list(input().split()) for _ in range(N)]
    # print(nodes)

    for i in range(len(nodes)-1, 0, -1):
        node = nodes[i]
        # print(i, node)
        idx = int(node[0])

        if len(node) == 4:
            l = int(node[2])
            r = int(node[3])
            tmp = calc(nodes[l][1], node[1], nodes[r][1])
            node[1] = tmp

    answer = int(nodes[1][1])
    print('#{} {}'.format(tc, answer))