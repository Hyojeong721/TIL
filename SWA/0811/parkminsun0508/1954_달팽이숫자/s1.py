#1954 달팽이숫자
# N 크기의 달팽이 출력
# 순서는 우 -> 하 -> 좌 -> 상 의 구조

import sys
sys.stdin = open("input.txt")
T = int(input())

# 달팽이 방향이니까 우 -> 하 -> 좌 -> 상 으로 돌 수 있도록 방향 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


for tc in range (1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 초기의 가로, 세로 위치, 회전방향 설정
    row = 0
    col = 0
    d = 0

    # 배열에 채울 숫자
    num = 1
    while num <= N*N:
        if 0 <= row < N and 0 <= col < N and not snail[row][col]:
            snail[row][col] = num
            num += 1
        # 범위에 속하지 않을 경우
        else:
            row -= dr[d]
            col -= dc[d]
            d = (d+1) % 4

        row += dr[d]
        col += dc[d]
    print("#{} ".format(tc))
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=" ")
        print()












