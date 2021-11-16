import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):

    # N*N = 보드 크기
    # K = 단어 길이
    N, K = list(map(int, input().split()))

    # 보드 오른쪽/아래에 0으로 채워진 한줄씩 추가
    board = [(list(map(int, input().split()))+[0]) for _ in range(N)]
    board.append([0]*(N+1))

    result = 0 # 가능한 경우의 수 총합

    # 가로
    for i in range(N):
        count_row = 0 # 연속으로 1이 나오면 +1
        for j in range(N):
            if board[i][j] == 0:
                count_row = 0
            if board[i][j] == 1:
                count_row += 1
                # 연속으로 1이 나온 수가 K랑 같고, 그 다음 칸에 1이 아니면 result에 +1
                if count_row == K and board[i][j+1] != 1:
                    result += 1

    # 세로
    for a in range(N):
        count_col = 0
        for b in range(N):
            if board[b][a] == 0:
                count_col = 0
            if board[b][a] == 1:
                count_col += 1
                if count_col == K and board[b+1][a] != 1:
                    result += 1

    print('#{} {}'.format(tc, result))