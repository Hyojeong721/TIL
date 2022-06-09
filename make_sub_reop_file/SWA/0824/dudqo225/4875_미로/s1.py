import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 상 우 좌 하 델타 리스트 생성
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 시작점과 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j


