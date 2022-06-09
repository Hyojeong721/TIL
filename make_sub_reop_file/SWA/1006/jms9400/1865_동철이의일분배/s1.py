import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(a, total):
    global answer

    if total <= answer:
        return

    if a == N:
        if answer <= total:
            answer = total
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(a+1, total * arr[a][i]/100)
            visited[i] = 0


for tc in range(1, T+1):
    answer = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    dfs(0, 1)
    print('#{} {:f}'.format(tc, answer * 100))
