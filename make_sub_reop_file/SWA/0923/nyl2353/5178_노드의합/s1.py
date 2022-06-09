import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 2)
    for _ in range(M):
        idx, value = map(int, input().split())
        tree[idx] = value

    if not N % 2:
        for i in range(N, 2, -2):
            tree[i//2] = tree[i] + tree[i+1]
    else:
        for j in range(N, 2, -2):
            tree[j//2] = tree[j] + tree[j-1]

    print('#{} {}'.format(tc, tree[L]))