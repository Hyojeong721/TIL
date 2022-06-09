import sys
sys.stdin = open('input.txt')


'''
아직 덜했음...
'''


T = int(input())
for tc in range(1, T+1):

    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    # visited = [list(False for _ in range(N)) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    # print(visited)

    # 상 우 하 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    # 출발점 좌표 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                # print(si, sj)

    for i in range(4):
        # 현재 위치
        ni = si + di[i]
        nj = sj + dj[i]
        if