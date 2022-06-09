import sys
sys.stdin = open('input.txt')

def count_nodes(N, nodes_by_p):
    global count
    if nodes_by_p[N]:
        for n in nodes_by_p[N]:
            count += 1
            count_nodes(n, nodes_by_p)


T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    nodes = list(map(int, (input().split())))
    nodes_by_p = [[] for _ in range(E+2)]
    for i in range(E):
        nodes_by_p[nodes[2 * i]].append(nodes[2 * i + 1])
    count = 1
    count_nodes(N, nodes_by_p)
    print('#{} {}'.format(test_case, count))