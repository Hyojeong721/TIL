import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ARR = [[0] * N for _ in range(N)]
    curR = 0
    curC = 0
    value = 1
    # 우, 하, 좌, 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    mode = 0

    while value <= N ** 2:
        # 1. 현재 좌표에 value 입력
        ARR[curR][curC] = value
        # 2. 다음번 데이터 입력을 위한 좌표 갱신
        # 2-1. 갱신을 위한 새로운 좌표 생성
        newR = curR + dr[mode]
        newC = curC + dc[mode]
        # 2-2. 새로운 좌표의 유효성 확인
        if newR < 0 or newR >= N or newC < 0 or newC >= N or ARR[newR][newC]:

            # 2-3. 유효하지 않은 경우, mode 변경
            mode = (mode + 1) % 4
        # 2-4. 좌표 갱신
        curR += dr[mode]
        curC += dc[mode]
        # 3. value 증가
        value += 1

    print('#{}'.format(test_case))
    for i in range(N):
        print(*ARR[i])

    # N = int(input())
    # ARR = [[0] * N for _ in range(N)]
    # curR, curC = 0, 0
    # value = 1
    # dr = [0, 1, 0, -1]
    # dc = [1, 0, -1, 0]
    # mode = 0
    # newR, newC = 0, 0
    # while value <= N * N:
    #     ARR[curR][curC] = value
    #     value += 1
    #     curR += dr[mode]
    #     curC += dc[mode]
    #
    #     if curR < 0 or curR >= N or curC < 0 or curC >= N or ARR[curR][curC]:
    #         curR -= dr[mode]
    #         curC -= dc[mode]
    #         mode = (mode + 1) % 4
    #         curR += dr[mode]
    #         curC += dc[mode]
    # print('#{}'.format(test_case))
    # for i in ARR:
    #     for j in i:
    #         print(j, end=' ')
    #     print()


    # dr = [0, 1, 0, -1]    # 우 하 좌 상
    # dc = [1, 0, -1, 0]
    # dr = [-1, 0, 1, 0]    # 상 우 하 좌
    # dc = [0, 1, 0, -1]
    # dr = [0, 1, 0, -1]    # 좌 하 우 상
    # dc = [-1, 0, 1, 0]
    # dr = [-1, 0, 1, 0]   # 상 좌 하 우
    # dc = [0, -1, 0, 1]
    # dr = [0, -1, 0, 1]     # 좌 상 우 하
    # dc = [-1, 0, 1, 0]




