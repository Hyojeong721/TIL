import sys
sys.stdin = open('input.txt')

# 3x3 box 검사 함수 정의
def box(x_index, y_index):
    global arr, numbers, result_box
    temp = []
    for i in range(3):
        for j in range(3):
            temp.append(arr[x_index + i][y_index + j])
    temp_set = set(temp)
    if temp_set == numbers:
        return result_box
    else:
        result_box = 0
        return result_box

T = int(input())

for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    result_row = 1
    result_col = 1
    result_box = 1
    result = 1

    # 가로줄 검사
    for i in range(9):
        row_set = set(arr[i])
        if row_set == numbers:
            pass
        else:
            result_row = 0
            break

    # 세로줄 검사
    for i in range(9):
        col_set = {}
        col_list = []
        for j in range(9):
            col_list.append(arr[j][i])
        col_set = set(col_list)
        if col_set == numbers:
            pass
        else:
            result_col = 0
            break

    # 3x3 box 검사
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                x_index = i
                y_index = j
                result = box(x_index, y_index)

    # 각 검사에서 이상이 있었으면 result=0으로
    if result_row + result_col + result_box < 3:
        result = 0


    print('#{} {}'.format(tc, result))


