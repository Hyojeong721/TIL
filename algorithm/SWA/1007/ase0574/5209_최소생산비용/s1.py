# 6/10 pass

import sys
sys.stdin = open('input.txt')
def bfs(cnt, ans):
    global min_ans, start

    if cnt == N:
        if start == 0:
            start = 1
            min_ans = ans

        elif min_ans >= ans:
            min_ans = ans
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            new_ans = ans + arr[cnt][i]
            bfs(cnt+1, new_ans)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_ans = 0
    start = 0

    bfs(0, 0)

    print("#{} {}".format(tc, min_ans))