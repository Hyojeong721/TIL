import sys
sys.stdin = open('input.txt')

T = int(input())

def check(now, visited):
    global mat, N, cnt
    if now == N:
        cnt += 1
        return

    for x in range(N):
        if visited[now][x]:
            continue
        else:
            visited[now][x] += 1
            for y in range(now):
                visited[now+y][x] += 1
                if 0 <= x+y < N:
                    visited[now+y][x+y] += 1
                if 0 <= x-y < N:
                    visited[now+y][x-y] += 1
            visited[now][x] += 1
            check(now+1, visited)
            visited[now][x] -= 1


for tc in range(1, T+1):
    N = int(input())
    mat = [[0]*N for _ in range(N)]
    cnt = 0
    check(0, mat)
    print(f'#{tc} {cnt}')