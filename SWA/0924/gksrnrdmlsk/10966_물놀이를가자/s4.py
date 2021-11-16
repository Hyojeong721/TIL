import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    answer = 0
    deq = [0] * (M * N + 100)
    start = 0
    end = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'W':
                deq[end] = (i, j)
                visited[i][j] = 0
                end += 1

    dx = [-1, 0, 1, 0]  # 상 우 하 좌
    dy = [0, 1, 0, -1]

    while start != end:
        x, y = deq[start]
        for k in range(4):
            xi = x + dx[k]  # 세로
            yi = y + dy[k]  # 가로
            if 0 <= xi < N and 0 <= yi < M and visited[xi][yi] == -1 and lst[xi][yi] == 'L':
                visited[xi][yi] = visited[x][y] + 1
                deq[end] = (xi, yi)
                end += 1
        start += 1

    for m in visited:
        answer += sum(m)

    print('#{} {}'.format(tc, answer))