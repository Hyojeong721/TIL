import sys
sys.stdin = open('input.txt')
"""
dfs, bfs 외에 풀이법으로 풀자!
1.
visited = [0] * N*N 방문체크
연속된 1의 개수 카운트(카운트배열)

2.
위치와 거리 저장
방번호가 인덱스인 리스트
pos = [0] * N*N  -> 위치 저장(r, c) 튜퓰 형식
dist = [1] * N*N 상하좌우 검색해서 1 작은 번호가 있다면 직전 값이랑 1씩 더해줌


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pos = [0] * (N * N + 1)
    dis = [1] * (N * N + 1)

    for i in range(N):
        for j in range(N):
            pos[arr[i][j]] = i, j

    for i in range(2, N*N+1):
        x1, x2, y1, y2 = pos[i][0], pos[i-1][0], pos[i][1], pos[i-1][1]
        if abs(x1-x2) + abs(y1-y2) == 1:
            dis[i] += dis[i- 1]

    t = max(dis)
    for i in range(1, N ** 2 + 1):
        if dis[i] == t:
            room = i - t + 1
            break

    print('#{} {} {}'.format(tc, room, t))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# def find(r, c, room, cnt):
#     global ans, room_num
#
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == arr[r][c] + 1:
#             find(nr, nc, arr[nr][nc], cnt + 1)
#
#     else:
#         if ans < cnt:
#             ans = cnt
#             room_num = room
#             return True
#         return False#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     room = 0
#     ans = 0
#     # print(arr)
#
#     for i in range(N):
#         for j in range(N):
#             find(i, j, arr[i][j], 1)
#
#
#     print('#{} {} {}'.format(tc, room_num-ans, ans))
##################################################################
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     visited = [0] * (N * N + 1)
#
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 ni = i + dr[k]
#                 nj = j + dc[k]
#                 if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
#                     visited[arr[i][j]] = 1
#
#     idx = 0
#     ans = 0
#     cnt = 0
#     for i in range(1, N*N+1):
#         if visited[i]:
#             cnt += 1
#         else:
#             if ans < cnt:
#                 ans = cnt
#                 idx = i - cnt
#             cnt = 0
#
#     print('#{} {} {}'.format(tc, idx, ans+1))
####################################################################


