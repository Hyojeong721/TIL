import sys
sys.stdin = open('input.txt')

"""

1. 최대이동가능 거리(시간)를 베이스로 하는 bfs를 만들어서 계산하자!
뭔가 bfs처럼 초음파 형식이 잘 맞아떨어질 것 같음
bfs
시작점: 현 위치
방문표시
우하좌상 인접한 좌표 검색, 미방문 and 이동가능한 곳이면
큐에 해당 좌표 넣기
 

"""
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


pipe = [[],
        [0, 1, 2, 3],
        [1, 3],
        [0, 2],
        [0, 3],
        [0, 1],
        [1, 2],
        [2, 3]
        ]

def bfs(arr, r, c, l):
    queue = [(r, c)]
    visited[r][c] = 1
    cnt = 0


    while queue:
        # for x in range(N):
        #     if l in visited[x]:
        #         return


        r, c = queue.pop(0)

        if visited[r][c] == l:
            continue

        for k in pipe[arr[r][c]]:
            nr = r + dr[k]
            nc = c + dc[k]

            # if 0 <= nr < N and 0 <= nc < M and arr[r][c] and not visited[nr][nc] and (k + 2) % 4 in pipe[arr[nr][nc]]:
            if 0 <= nr < N and 0 <= nc < M and arr[r][c] and not visited[nr][nc]:
                cp = arr[r][c]
                np = arr[nr][nc]
                # if (k + 2) % 4 in pipe[arr[nr][nc]]:
                # visited[nr][nc] = visited[r][c] + 1
                #
                # queue.append((nr, nc))
    # return
    #             if not (k + 2) % 4 in pipe[arr[nr][nc]]: continue
                if k == 0 and 0 in pipe[cp] and 2 in pipe[np]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
                elif k == 1 and 1 in pipe[cp] and 3 in pipe[np]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

                elif k == 2 and 2 in pipe[cp] and 0 in pipe[np]:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

                else:
                    if k == 3 and 3 in pipe[cp] and 1 in pipe[np]:
                        visited[nr][nc] = visited[r][c] + 1
                        queue.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))
    # print(arr)

    visited = list([0] * M for _ in range(N))

    bfs(arr, R, C, L)

    ans = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                ans += 1

    print('#{} {}'.format(tc, ans))



# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# pipe = [
#     [],
#     [0, 1, 2, 3],
#     [1, 3],
#     [0, 2],
#     [0, 3],
#     [0, 1],
#     [1, 2],
#     [2, 3]
# ]
#
#
# def DFS(r, c, time):
#     visited[r][c] = time
#     if time == L: return
#
#     for i in pipe[tunnel[r][c]]:
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if 0 <= nr < N and 0 <= nc < M and\
#                 tunnel[nr][nc] and\
#                 ((i + 2) % 4 in pipe[tunnel[nr][nc]]) and\
#                 visited[nr][nc] > time:
#             DFS(nr, nc, time + 1)
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     # 지도 정보
#     tunnel = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[987654321] * M for _ in range(N)]  # 방문 체크
#
#     DFS(R, C, 1)
#
#     ans = 0
#
#     for i in range(N):
#         for j in range(M):
#             if visited[i][j] != 987654321:
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))
