import sys
sys.stdin = open('input.txt')


# def check(s):
#     global maze
#     visited = [[0] * N for _ in range(N)]
#
#     i, j = s
#
#
#     for mode in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#         i += mode[0]
#         j += mode[1]
#
#         if  0 <= i < N and 0 <= j < N and maze[i][j] == 3:
#             return 1
#
#         if 0 <= i < N and 0 <= j < N and visited[i][j] == 0 and (maze[i][j] == 0 or maze[i][j] == 3):
#             return check((i, j))






def dfs(s):
    global maze

    visited = [[0] * N for _ in range(N)]

    # s: 시작점 좌표 (tuple 형식)
    stack = [s]

    while stack:
        # v: 현재 위치 좌표
        v = stack.pop()
        i = v[0]   # i: 현재 위치의 세로 좌표(행)
        j = v[1]   # j: 현재 위치의 가로 좌표(열)

        # 3에 도착하면 함수 종료
        if maze[i][j] == 3:
            return 1

        # 방문한 곳은 visited에 1로 기록
        if visited[i][j] == 0:
            visited[i][j] = 1
            # 현재 위치에서 우, 하, 좌, 상으로 한칸씩 이동할 수 있는지 검토
            for k in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + k[0]
                nj = j + k[1]
                # 이동할 수 있는 좌표이면, 그 좌표(w)를 stack에 push
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and (maze[ni][nj] == 0 or maze[ni][nj] == 3):
                    w = (ni, nj)
                    stack.append(w)
    # 3에 도착하지 못하면 함수 종료
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                # start: 시작 위치 좌표
                start = (i, j)

    print('#{} {}'.format(tc, dfs(start)))