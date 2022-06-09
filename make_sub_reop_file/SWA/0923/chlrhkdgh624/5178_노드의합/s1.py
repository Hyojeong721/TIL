import sys
sys.stdin = open('input.txt')
T = int(input())


def node_sum(x):
    if x//2 == 0:
        return
    if tree[x//2] == 0:
        if x % 2 == 0:
            try:
                tree[x//2] = tree[x] + tree[x+1]
            except IndexError:
                tree[x//2] = tree[x]
        else:
            tree[x//2] = tree[x] + tree[x-1]


for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        node, number = map(int, input().split())
        tree[node] = number

    for i in range(N, 0, -1):
        node_sum(i)

    print(f'#{tc} {tree[L]}')
