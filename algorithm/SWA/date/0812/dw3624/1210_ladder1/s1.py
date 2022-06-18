import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    t = int(input())
    mat = []

    # 양측에 padding 추가, 102 * 100 matrix 생성
    tmp_mat = [list(map(int, input().split())) for _ in range(100)]
    for tmp_row in tmp_mat:
        tmp_row.insert(0, 0)
        tmp_row.append(0)
        mat.append(tmp_row)

    # 도착점(col==2)인 지점의 idx 탐색
    row, col = 99, 0
    for m in range(len(mat[-1])):
        if mat[-1][m] == 2:
            col = m
            break

    # 방향변환 횟수를 count하는 변수
    # 짝수번 방향변환 : 위로 이동
    # 홀수번 방향변환 : 좌우로 이동
    trans = 0
    while row > 0:
        # 좌우 이동
        if trans % 2:
            # 좌측에 경로 있는 경우
            if mat[row][col-1] == 1:
                col -= 1
                while mat[row-1][col] == 0 and mat[row+1][col] == 0:
                    col -= 1

            # 우측에 경로 있는 경우
            elif mat[row][col+1] == 1:
                col += 1
                while mat[row-1][col] == 0 and mat[row+1][col] == 0:
                    col += 1
            trans += 1

        # 상방향 이동
        else:
            row -= 1
            while mat[row][col-1] == 0 and mat[row][col+1] == 0 and row > 0:
                row -= 1
            trans += 1

    # padding 제거한 col idx
    result = col -1
    print('#{} {}'.format(t, result))
