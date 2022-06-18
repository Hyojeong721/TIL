'''

소생시키려 노력중 ^^!

'''

import sys
sys.stdin = open('input.txt')

def get_num_fitted_words(puzzle, N, K):
    cnt = 0

    # 탐색 구간
    for search_r in range(N - K + 1):
        for search_c in range(N - K + 1):
            # 세로로 K개 탐색
            cnt_r = 0
            for r in range(search_r, search_r + K):
                cnt_r += puzzle[r][search_c]

            # 세로 K개가 전부 흰색이면 위,아래 검은색인지 검사
            if cnt_r == K:
                if K == N:
                    cnt += 1
                elif search_r == 0 and puzzle[search_r + K][search_c] == 0:
                    cnt += 1
                elif search_r == N - K and puzzle[search_r - 1][search_c] == 0:
                    cnt += 1
                elif puzzle[search_r - 1][search_c] + puzzle[search_r + K][search_c] == 0:
                    cnt += 1

            # # 가로로 K개 탐색
            # cnt_c = 0
            # for c in range(search_c, search_c + K):
            #     cnt_c += puzzle[search_r][c]
            #
            # # 가로 K개가 전부 흰색이면 왼,오오검은색인지 검사
            # if cnt_c == K:
            #     if K == N:
            #         cnt += 1
            #     elif search_c == 0 and puzzle[search_r][search_c + K] == 0:
            #         cnt += 1
            #     elif search_c == N - K and puzzle[search_r][search_c - 1] == 0:
            #         cnt += 1
            #     elif puzzle[search_r][search_c - 1] + puzzle[search_r][search_c + K] == 0:
            #         cnt += 1

    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    result = get_num_fitted_words(puzzle, N, K)
    print('#{0} {1}'.format(tc, result))