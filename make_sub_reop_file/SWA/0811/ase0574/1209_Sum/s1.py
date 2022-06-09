import sys
sys.stdin = open('input.txt')
# 배열의 크기는 100X100으로 동일
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    cross_add = 0

    result = []

    # 행 합
    max_col = max_row = 0
    for i in range(100):
        row_add = 0
        col_add = 0
        for j in range(100):
            row_add += arr[i][j]
            col_add += arr[j][i]
        # 행합 중 최대값
        if max_row < row_add:
            max_row = row_add
        # 열 합 중 최대값
        if max_col < col_add:
            max_col = col_add
    # 대각선 합
    for k in range(N):
        cross_add += arr[k][k]

    result.append(max_row)
    result.append(max_col)
    result.append(cross_add)
    # 모든 합들중 최댓값 출력
    print("#{} {}".format(tc, max(result)))