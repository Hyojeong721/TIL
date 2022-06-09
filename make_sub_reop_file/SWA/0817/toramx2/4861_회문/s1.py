import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    # N, M, board 정의
    N, M = list(map(int, input().split()))
    board = [[0] * N for _ in range(N)]
    for row in range(N):
        tmp = input()
        for col in range(N):
            board[row][col] = tmp[col]

    # board를 M*M 크기로 자르고 가로 혹은 세로에 회문이 있는지 확인
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 가로줄
            for ni in range(i, i+M):
                char = ''
                for nj in range(j, j+M):
                    char += board[ni][nj]
                if char == char[::-1]:
                    result = char

            # 세로줄
            for ni in range(i, i+M):
                char = ''
                for nj in range(j, j+M):
                    char += board[nj][ni]
                if char == char[::-1]:
                    result = char

    print('#{0} {1}'.format(test_case, result))



