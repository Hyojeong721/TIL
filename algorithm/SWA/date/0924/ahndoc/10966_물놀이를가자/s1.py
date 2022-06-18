import sys
sys.stdin = open('input.txt')
"""
최소 이동 횟수 구하기 = BFS

    1) 리스트 queue => 시간초과
    2) deque => from collections import deque
    3) 선형큐 (front, rear)
    4) 원형큐
    5) 연결리스트 queue


1. 시작점인 W를 몽땅 찾아서 큐에 담아두기(2차원 리스트 전체 돌기)
2. visited의 물의 위치(W의 좌표)는 0으로 바꿔주기
    (큐에 좌표를 집어넣으면서 방문체크하는 경우임)
3. while Q:
    큐에서 좌표 빼오기
    for 인근 좌표 접근
        visited에 방문체크 겸 거리체크
        Q에 좌표 넣어주기

점 v의 방문표시 코드를 어디에 위치하는지에 따라 차이가 생김
    '''
    
    '''


"""
# from collections import deque
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     board = list(input() for _ in range(N))
#     # print(board)
#
#     visited = list([987654321] * M for _ in range(N))

    # q = [0] * M * N
    # front = -1  # 뺄 때 사용
    # rear = -1   # 넣을 때 사용
    #
    # # q = deque()
    #
    # for i in range(N):
    #     for j in range(M):
    #         if board[i][j] == 'W':
    #             visited[i][j] = 0
    #             # q.append((i, j))
    #             rear += 1
    #             q[rear] = (i, j)
    #
    # # while q:
    # while front != rear:
    #     # r, c = q.popleft()
    #     front += 1
    #     r, c = q[front]
    #
    #     for i in range(4):
    #         nr = r + dr[i]
    #         nc = c + dc[i]
    #
    #         if nr < 0 or nr >= N or nc < 0 or nc >= M:continue
    #         # if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 987654321:
    #         #     q.append((nr, nc))
    #         #     visited[nr][nc] = visited[r][c] + 1
    #         if visited[nr][nc] == 987654321 and board[nr][nc] == 'L':
    #             # q.append((nr, nc))
    #             rear += 1
    #             q[rear] = (nr, nc)
    #             visited[nr][nc] = visited[r][c] + 1
    #
    # ans = 0
    #
    # for i in visited:
    #     ans += sum(i)
    #
    # print('#{} {}'.format(tc, ans))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     board = [input() for _ in range(N)]
#
#     visited = [[-1] * M for _ in range(N)]
#
#     queue = [0] * N * M
#     front = -1
#     rear = -1
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 'W':
#                 visited[i][j] = 0
#                 rear += 1
#                 queue[rear] = (i, j)
#
#     while front != rear:
#         front += 1
#         r, c = queue[front]
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc] != -1:continue
#             if board[nr][nc] == 'L':
#                 visited[nr][nc] = visited[r][c] + 1
#                 rear += 1
#                 queue[rear] = (nr, nc)
#
#     ans = 0
#     for i in visited:
#         for j in i:
#             ans += j
#
#     print('#{} {}'.format(tc, ans))

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    visited = list([0] * M for _ in range(N))
    print(arr)
    print(visited)

    # bfs
    q = [0] * N * M
    front = -1
    rear = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                # q.append((i, j))
                rear += 1
                q[rear] = (i, j)

    while front != rear:
        # r, c = q.pop(0)
        front += 1
        r, c = q[front]

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                rear += 1
                q[rear] = (nr, nc)
                # q.append((nr, nc))
                # if visited[nr][nc] < visited[r][c]:
    ans = 0
    for i in range(N):
        ans += sum(visited[i])

    print('#{} {}'.format(tc, ans))





