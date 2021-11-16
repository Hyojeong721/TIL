import sys
sys.stdin = open('input.txt')

# N * N 행렬에서 이웃 요소와 차이의 절댓값 합을 구하는 함수
def get_sum_abs(N, mat):
    total = 0
    for i in range(N):
        for j in range(N):
            if j != N - 1:
                diff_row = mat[i][j] - mat[i][j + 1]
                total += diff_row if diff_row > 0 else - diff_row
            if i != N - 1:
                diff_col = mat[i][j] - mat[i + 1][j]
                total += diff_col if diff_col > 0 else - diff_col
    return 2 * total

# 테스트 케이스마다 진행
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = []
    for _ in range(N):
        mat.append(list(map(int, input().split())))
    sum_abs = get_sum_abs(N, mat)
    print('#{0} {1}'.format(tc, sum_abs))
