import sys
sys.stdin = open('input.txt')

# def check():
#     for i in range(9):
#         # 체크를 위한
#         row = [0] * 10
#         col = [0] * 10
#
#         for j in range(9):
#             # 행을 검사
#             num_row = sudoku[i][j]
#             # 열을 검사
#             num_col = sudoku[j][i]
#
#             # 이미 사용한 숫자라면 종료
#             if row[num_row]: return 0
#             if col[num_col]: return 0
#
#             row[num_row] = 1
#             col[num_col] = 1
#
#             ###################
#             # 3x3 검사도 한번에 처리
#             if i % 3 == 0 and j % 3 == 0:
#                 square = [0] * 10
#                 for r in range(i, i+3):
#                     for c in range(j, j+3):
#                         num = sudoku[r][c]
#                         # 중복된 숫자가 나오면 종료
#                         if square[num]: return 0
#                         square[num] = 1
#     return 1
#
# T = int(input())
# for tc in range(1, T+1):
#     sudoku = [list(map(int, input().split())) for _ in range(9)]
#
#     print('#{} {}'.format(tc, check()))

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    cnt = 0
    for i in range(9):
        if cnt == 1:
            break
        cnt_row = [0] * 10
        cnt_col = [0] * 10
        for j in range(9):
            cnt_row[arr[i][j]] = 1
            cnt_col[arr[j][i]] = 1

            if i % 3 == 0 and j % 3 == 0:
                delta = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
                cnt_square = [0] * 10
                for k in delta:
                    cnt_square[arr[i + k[0]][j + k[1]]] = 1
                if cnt_square.count(1) != 9:
                    result = 0
                    cnt += 1
                    break
        if cnt_row.count(1) != 9:
            result = 0
            break
        if cnt_col.count(1) != 9:
            result = 0
            break

    print('#{} {}'.format(tc, result))
