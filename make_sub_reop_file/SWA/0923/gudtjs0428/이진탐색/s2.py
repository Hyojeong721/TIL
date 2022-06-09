import sys
import math
sys.stdin = open('input.txt')

def bi_nodes(root):
    j = 0
    oper = root
    global nodes
    for i in range(int(math.log(N, 2))):
        oper = oper // 2
        k = 0
        while j < N-1 and k < 2**(i+1):
            n = root - oper
            nodes.append(n)
            j += 1
            k += 1
            m = root + oper
            nodes.append(m)
            j += 1
            k += 1


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    root = N // 2 + 1
    nodes = [root]
    bi_nodes(root)
    print('#{} {} {}'.format(test_case, root, nodes[2//N]))