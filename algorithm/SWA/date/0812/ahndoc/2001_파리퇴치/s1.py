import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            temp = 0
            for dr in range(M):
                for dc in range(M):
                    ni = i + dr
                    nj = j + dc
                    # 인덱스 범위 벗어나지 않도록 조건 설정
                    if 0 <= ni < N and 0 <= nj < N:
                        temp += board[ni][nj]
            if temp > max_v:
                max_v = temp
    print('#{} {}'.format(test_case, max_v))

    # max_v = 0
    # # N x N 보드 위에 M x M 칸 파리채를 칠 수 있는 범위는? (N-M+1) x (N-M+1)
    # for i in range(N-M+1):
    #     for j in range(N-M+1):
    #         temp = 0
    #         for dr in range(M):
    #             for dc in range(M):
    #                 ni = i + dr
    #                 nj = j + dc
    #                 temp += board[ni][nj]
    #         if temp > max_v:
    #             max_v = temp
    # print('#{} {}'.format(test_case, max_v))












############################################################
    # N, M =map(int, input().split())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    #
    # max_v = 0
    # for i in range(N - M + 1):
    #     for j in range(N - M + 1):
    #         sum_v = 0
    #
    #         for dr in range(M):
    #             for dc in range(M):
    #                 sum_v += arr[i+dr][j+dc]
    #         if sum_v > max_v:
    #             max_v = sum_v
    #
    # print('#{} {}'.format(test_case, max_v))

