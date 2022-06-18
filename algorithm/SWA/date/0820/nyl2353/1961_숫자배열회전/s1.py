import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 행렬 3가지 회전하기
    mat1 = []   # 90도 회전
    mat2 = []   # 180도 회전
    mat3 = []   # 270도 회전
    for i in range(N):
        row1 = ''
        row2 = ''
        row3 = ''
        for j in range(N):
            row1 += str(mat[N-1-j][i])
            row2 += str(mat[N-1-i][N-1-j])
            row3 += str(mat[j][N-1-i])
        mat1.append(row1)
        mat2.append(row2)
        mat3.append(row3)

    # 회전된 행렬 모음
    rotated = [mat1, mat2, mat3]

    # 출력
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(3):
            print(rotated[j][i], end=' ')
        print()