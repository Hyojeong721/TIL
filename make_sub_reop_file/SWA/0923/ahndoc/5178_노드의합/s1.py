import sys
sys.stdin = open('input.txt')




T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    leaf_nodes = []
    for _ in range(M):
        leaf_nodes.append(list(map(int, input().split())))

    tree = [0] * (N + 1)
    for node in leaf_nodes:
        if tree[node[0]] == 0:
            tree[node[0]] = node[1]

    # print(tree)
    while N > 1:
        if N % 2:
            c = N - 1
            p = c // 2
            if tree[p] == 0:
                tree[p] = tree[c] + tree[c+1]
        else:
            c = N
            p = c // 2
            if tree[p] == 0:
                tree[p] = tree[c]
        N -= 1

    print('#{} {}'.format(tc, tree[L]))

