import sys
sys.stdin = open('input.txt')

"""
1. 가장 높은 봉우리 좌표를 찾는다. (여러개 나올 수 있음)
2. 가장 높은 봉우리 좌표에서 모두 출발시킨다. (DFS로)
3. DFS 만들기
    1) 큰 틀: visited에 현재 좌표 기록 -> 델타값 이용하여 4방향 검토 후 이동  
    2) 똑같은 크기로 visited를 만들어서 지나간 곳 방문 체크
    3) 모든 경로를 지나가기 위해서는 되돌아올 때 visited의 방문 기록을 지워야 함
    
    4) 모든 경로를 탐색하는 DFS 구조(visited 기록 해제 버전)
    '''     
     visited 방문한 곳 1 넣어주면서 체크
     for 반복문으로 근처 좌표에 접근
        dfs 호출
     (dfs 빠져나온 뒤) 
     visited 방문했던 곳 0 넣어주면서 체크 해제    
    '''  

    
"""

# 우하좌상
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# # 1. 현재 위치를 들고 다니지 않을 때
# # r, c: 좌표, road: 현재까지 조성된 등산로의 길이, skill: 공사 유무
# def work(r, c, road, skill):
#     global ans
#     if road > ans: ans = road
#
#     visited[r][c] = 1
#
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#             # 현 위치보다 낮은 곳으로 이동하는 경우
#             if arr[nr][nc] < arr[r][c]:
#                 work(nr, nc, road+1, skill)
#             # 현 위치보다 높거나 같은 곳으로 이동하는 경우
#             elif skill and arr[nr][nc] - K < arr[r][c]:
#                 tmp = arr[nr][nc]
#                 arr[nr][nc] = arr[r][c] - 1
#                 work(nr, nc, road+1, 0)
#                 arr[nr][nc] = tmp
#
#     visited[r][c] = 0
#
# # 2. 현재 위치를 들고다니는 방법
# def work2(r, c, h, road, skill):
#     global ans
#     if road > ans: ans = road
#     visited[r][c] = 1
#
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]: continue
#
#
#         if h > arr[nr][nc]:
#             work2(nr, nc, arr[nr][nc], road+1, skill)
#         elif skill and h > arr[nr][nc] - K:
#             work2(nr, nc, arr[r][c]-1, road+1, 0)
#
#     visited[r][c] = 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split()) # N: 한변의 길이, K: 최대 공사가 가능한 깊이
#
#     # N*N 크기의 2차원 리스트(배열)이 주어진다.
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # print(arr)
#
#     # 최고 높이의 봉우리를 찾는 과정
#     max_h = 0
#     for i in range(N):
#         for j in range(N):
#             if max_h < arr[i][j]:
#                 max_h = arr[i][j]
#
#     # 한줄씩 입력 받으면서 최대 높이의 봉우리를 찾는 코드
#     # arr = []
#     # max_h = 0
#     # for i in range(N):
#     #     tmp = list(map(int, input().split()))
#     #
#     #     for j in tmp:
#     #         if max_h < j:
#     #             max_h = j
#     #     arr.append(tmp)
#
#     # print(max_h)
#
#     visited = [[0] * N for _ in range(N)]
#     ans = 0
#
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == max_h:
#                 # work(i, j, 1, 1) # 좌표, 길, 스킬
#                 work2(i, j, max_h, 1, 1)  # 좌표, 높이, 길, 스킬
#
#     print(ans)

############################################################################

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:continue

        if mountain[nr][nc] < mountain[r][c]:
            dfs(nr, nc, road+1, skill)
        elif skill and mountain[nr][nc] - K < mountain[r][c]:
            tmp = mountain[nr][nc]
            mountain[nr][nc] = mountain[r][c] - 1
            dfs(nr, nc, road+1, 0)
            mountain[nr][nc] = tmp

    visited[r][c] = 0

# 최대 높이 들고 다니기
def dfs2(r, c, h, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if mountain[nr][nc] < h:
                dfs2(nr, nc, mountain[nr][nc], road+1, skill)
            elif skill and mountain[nr][nc] - K < h:
                dfs2(nr, nc, h - 1, road+1, 0)

    visited[r][c] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = []

    max_h = 0
    for i in range(N):
        tmp = list(map(int, input().split()))
        mountain.append(tmp)
        for j in tmp:
            if j > max_h:
                max_h = j
    # print(mountain)

    visited = [[0] * N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                # dfs(i, j, 1, 1)
                dfs2(i, j, max_h, 1, 1)

    print('#{} {}'.format(tc, ans))

