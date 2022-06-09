import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    w_check = [0 for _ in range(N)]
    t_check = [0 for _ in range(M)]

    for t in range(M):
        idx = -1
        for w in range(N):
            if not w_check[w] and t_check[t] < weights[w] <= trucks[t]:
                t_check[t] = weights[w]
                idx = w
        if idx != -1:
            w_check[idx] = 1

    print('#{} {}'.format(tc, sum(t_check)))