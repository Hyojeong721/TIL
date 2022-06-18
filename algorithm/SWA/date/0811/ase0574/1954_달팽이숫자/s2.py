# 0829
import sys
sys.stdin = open('input.txt')
# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력

T = int(input())
for tc in range(1, T+1):
    # N x N 배열
    N = int(input())
    arr = [[0 for _ in range(N)]for _ in range(N)]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1
    k = 0
    x = 0
    y = -1

    # 달팽이 움직이기 시작!
    while cnt <= (N * N):
        new_x = x + dx[k % 4]
        new_y = y + dy[k % 4]
        if 0 <= new_x < N and 0 <= new_y < N and arr[new_x][new_y] == 0:
            arr[new_x][new_y] = cnt
            cnt += 1
            x = new_x
            y = new_y
        else:
            k += 1

        # 출력 양식
    print("#{}".format(tc))
    for i in range(N):
        print(*arr[i])
