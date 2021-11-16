import sys
import math
sys.stdin = open('input.txt')

def bi_nodes(N, root, oper, count):
    global nodes
    global i
    oper = oper // 2
    while count < int(math.log(N, 2)) and i < N:
        n = root - oper
        nodes.append(n)
        i += 1
        m = root + oper
        nodes.append(m)
        i += 1
        count += 1
        bi_nodes(N, n, oper, count)
        bi_nodes(N, m, oper, count)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    root = N // 2 + 1
    nodes = [root]
    oper = root
    i = 1
    count = 0
    bi_nodes(N, root, oper, count)
    if i > N:
        nodes.pop()
    print('#{} {} {}'.format(test_case, root, nodes[N//2-1]))