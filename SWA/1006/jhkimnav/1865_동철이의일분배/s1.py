import sys
sys.stdin = open('input.txt')

def norm(i):
    return int(i) / 100

def dfs(s, total_p):
    global max_p

    if total_p <= max_p:
        return

    if s == N:
        if total_p > max_p:
            max_p = total_p
    else:
        for i in range(N):
            if not visited[i] and arr[s][i]:
                visited[i] = 1
                total_p *= arr[s][i]
                dfs(s+1, total_p)
                visited[i] = 0
                total_p /= arr[s][i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(norm, input().split())) for _ in range(N)]

    visited = [0] * N
    max_p = 0
    # print(arr)
    dfs(0, 1)
    # print('#{} {}'.format(tc, round(max_p*100, 7)))
    print('#{} {}'.format(tc, format(max_p*100, '.6f')))