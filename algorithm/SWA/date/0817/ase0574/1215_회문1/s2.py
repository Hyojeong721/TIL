# 0824
import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    # 회문의 길이
    N = int(input())
    # 8X8 글자판
    arr = [list(map(str, input())) for _ in range(8)]
    cnt_row = 0
    cnt_col = 0

    # 행 검사
    for i in range(8):
        for j in range(8-N +1):
            result_row = ''
            for char in range(N):
                result_row += arr[i][j+char]
            # 회문 검사
            if result_row == result_row[::-1]:
                cnt_row += 1

    # 열 검사
    for i in range(8-N+1):
        for j in range(8):
            result_col = ''
            for char in range(N):
                result_col += arr[i+char][j]
            # 회문 검사
            if result_col == result_col[::-1]:
                cnt_col += 1

    print("#{} {}".format(tc, cnt_row + cnt_col))

