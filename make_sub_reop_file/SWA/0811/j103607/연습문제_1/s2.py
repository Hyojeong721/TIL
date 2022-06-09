import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                di = i + di[k]
                dj = j + dj[k]
                if 0 <= di < N and 0 <= dj < N:
