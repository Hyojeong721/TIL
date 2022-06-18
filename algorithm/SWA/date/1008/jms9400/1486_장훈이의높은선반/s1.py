import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(k, s):  # s 직원들의 키의 합
    global ans

    if s == H:
        ans = s
        return

    elif s > H:
        if s < ans:
            ans = s
        return

    for i in range(k, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, s + lst[i])
            visited[i] = 0


for tc in range(1, T+1):
    N, H = map(int, input().split())  # 점원의 수, 만들어야하는 높이
    lst = sorted(list(map(int, input().split())))
    visited = [0] * N
    ans = 987654321
    dfs(0, 0)

    print('#{} {}'.format(tc, ans - H))



