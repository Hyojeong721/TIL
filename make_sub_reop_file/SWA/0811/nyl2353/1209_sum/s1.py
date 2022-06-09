import sys
sys.stdin = open('input.txt')

def get_max_sum(mat, N=100):
    max_sum = mat[0][0]
    diagonal_right = 0
    diagonal_left = 0

    for i in range(N):
        sum_row = 0
        sum_col = 0
        for j in range(N):
            sum_row += mat[i][j]
            sum_col += mat[j][i]
        if sum_row > max_sum:
            max_sum = sum_row
        if sum_col > max_sum:
            max_sum = sum_col

        diagonal_left += mat[i][N - 1 - i]
        diagonal_right += mat[i][i]

    if diagonal_left > max_sum:
        max_sum = diagonal_left
    if diagonal_right > max_sum:
        max_sum = diagonal_right

    return max_sum

for _ in range(10):
    tc = int(input())
    mat = []
    for _ in range(100):
        mat.append(list(map(int, input().split())))
    max_sum = get_max_sum(mat)
    print('#{0} {1}'.format(tc, max_sum))
