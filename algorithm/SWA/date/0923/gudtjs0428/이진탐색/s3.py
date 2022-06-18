import sys
import math
sys.stdin = open('input.txt')

def bi_nodes(N, oper):
    global nodes
    global i
    tmp = []
    for row in nodes:
        if oper != 1:
            oper = oper // 2
        for node in row:
            tmp.append(node - oper)
            tmp.append(node + oper)
            i += 2
            if i > N:
                nodes.append(tmp)
                return
        nodes.append(tmp)
        tmp = []


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    root = ((int(math.log(N, 2))+1) ** 2) // 2
    nodes = [[root]]
    oper = root
    i = 1
    bi_nodes(N, oper)
    result = []
    for row in nodes:
        for node in row:
            result.append(node)
    print('#{} {} {}'.format(test_case, root, result[N//2-1]))