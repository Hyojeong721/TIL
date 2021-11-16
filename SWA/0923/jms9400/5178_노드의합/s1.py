import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # 10, 5, 2
    lst = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)
    for i in lst:
        tree[i[0]] = i[1]

    while tree[1] == 0:
        a = N // 2
        tree[a] += tree[N]
        N -= 1

    print('#{} {}'.format(tc, tree[L]))