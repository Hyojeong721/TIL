import sys
sys.stdin = open('input.txt')


def dfs(idx, cost):
    global min_cost

    if cost > min_cost:
        return

    if idx == N:
        if cost < min_cost:
            min_cost = cost
            return

    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                dfs(idx+1, cost + arr[idx][j])
                visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_cost = N * 100
    dfs(0, 0)

    print('#{} {}'.format(tc, min_cost))

