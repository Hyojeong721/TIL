from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]
    answer = 0
    deq = deque()

    for i in range(N):
        for j in range(M):
            if lst[i][j] == 'W':
                deq.append((i, j))
                visited[i][j] = 0

    dx = [-1, 0, 1, 0]  # 상 우 하 좌
    dy = [0, 1, 0, -1]

    while deq:
        x, y = deq.popleft()
        for k in range(4):
            xi = x + dx[k]  # 세로
            yi = y + dy[k]  # 가로
            if 0 <= xi < N and 0 <= yi < M and (visited[xi][yi] == -1 or visited[xi][yi] > visited[x][y]+1):  # 새로갈곳이 원래있던곳보다 크기가 작아야 감
                if lst[xi][yi] == 'L':
                    visited[xi][yi] = visited[x][y] + 1
                    deq.append((xi, yi))

    for m in visited:
        answer += sum(m)

    print('#{} {}'.format(tc, answer))