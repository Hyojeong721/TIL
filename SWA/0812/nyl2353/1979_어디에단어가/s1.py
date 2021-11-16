import sys
sys.stdin = open('input.txt')

def get_num_fitted_words(puzzle, N, K):
    """
    N * N 크기의 단어 퍼즐에서, 딱 K 길이만큼 빈 칸의 개수를 세는 함수
    puzzle: N * N 단어 퍼즐
    N: 퍼즐의 한 변 크기
    K: 원하는 빈 칸 크기

    """
    # 딱 맞는 빈 칸 카운팅
    cnt = 0

    for r in range(N):
        # 가로방향, 세로방향 빈 칸 길이 측정 값
        r_white = 0
        c_white = 0
        for c in range(N):
            # 1. 가로 방향 탐색
            # 흰 칸이면 측정 길이 + 1
            if puzzle[r][c]:
                r_white += 1
            # 검은 칸이면 조건 체크한 후, 길이 0으로 초기화
            else:
                # 앞까지의 흰칸이 K개면 카운트 +1
                if r_white == K:
                    cnt += 1
                r_white = 0

            # 2. 세로 방향 탐색
            if puzzle[c][r]:
                c_white += 1
            else:
                if c_white == K:
                    cnt += 1
                c_white = 0

        # 1-1. 가로 방향 흰 칸으로 끝난 경우 확인
        if r_white == K:
            cnt += 1

        # 2-1. 세로 방향 흰 칸으로 끝난 경우 확인
        if c_white == K:
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    result = get_num_fitted_words(puzzle, N, K)
    print('#{0} {1}'.format(tc, result))