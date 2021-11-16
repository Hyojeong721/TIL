import sys
sys.stdin = open("input.txt")

"""
문제 : 정수 N을 입력받아 N 크기의 달팽이를 출력하시오.
달팽이 : 1부터 N * N까지의 숫자가 시계방향으로 이루어져 있는 이차원 리스트

"""
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 0으로 이루어진 N * N 배열을 생성한다.
    arr = [[0] * N for _ in range(N)]

    # 델타탐색 초기값 설정한다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0

    # 초기 위치 설정한다.
    i, j = 0, -1

    # 배열 각 항목에 더할 수를 1부터 설정한다.
    cnt = 1

    while cnt <= N * N:
        ni = i + di[k]
        nj = j + dj[k]

        # 하나씩 위치를 옮겨가며 숫자를 추가한다.
        if 0 <= ni < N  and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        # 1) 벽을 만나면 2) 이미 0 아닌 수가 있다면 방향을 바꾼다. 순서는 우, 하, 좌, 상
        else:
            k = (k + 1) % 4

    print("#{}".format(tc))

    # 이차원 리스트를 다시 숫자로 바꾼다.
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = " ")
        print()