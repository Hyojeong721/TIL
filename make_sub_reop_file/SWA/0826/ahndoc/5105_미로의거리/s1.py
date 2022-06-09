import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = i, j
            if maze[i][j] == 3:
                goal = i, j

    queue = [start]

    visited = [[0] * N for _ in range(N)]
    visited[start[0]][start[1]] = 1
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    while queue:
        now = queue.pop(0)

        if maze[now[0]][now[1]] == 3:
            break
        # 현재 위치에서 우, 하, 좌, 상 탐색 후 이동 가능한 곳으로 이동
        for k in range(4):
            ni = now[0] + dr[k]
            nj = now[1] + dc[k]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[now[0]][now[1]] + 1


    if visited[goal[0]][goal[1]]:
        result = visited[goal[0]][goal[1]] - 2

    print('#{} {}'.format(tc, result))



