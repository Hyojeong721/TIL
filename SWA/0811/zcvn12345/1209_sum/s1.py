import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    t = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    sum_x, sum_y, sum_z = [], [], []
    tmp_z1 = 0
    tmp_z2 = 0
    for i in range(len(matrix)):
        tmp_z1 += matrix[i][i]
        tmp_z2 += matrix[i][100 - 1 - i]

        tmp_x = 0
        tmp_y = 0
        for j in range(len(matrix)):
            tmp_x += matrix[i][j]
            tmp_y += matrix[j][i]

        sum_x.append(tmp_x)
        sum_y.append(tmp_y)
    sum_z.extend([tmp_z1, tmp_z2])


    # 가장 큰 수 탐색
    sum_xyz = sum_x + sum_y + sum_z
    result = 0

    for k in range(len(sum_xyz)):
        if sum_xyz[k] > result:
            result = sum_xyz[k]

    print('#{} {}'.format(t, result))