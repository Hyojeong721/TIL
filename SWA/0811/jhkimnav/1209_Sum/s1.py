import sys
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    test_case = int(input())
    arr = [[0] * 100 for i in range(100)]
    for i in range(100):
        arr[i] = list(map(int, input().split()))
    max_value = 0
    # 우하향 대각선
    sum_of_right_diagonal = 0
    
    # 좌상향 대각선
    sum_of_left_diagonal = 0
    for i in range(100):
        sum_of_col = 0
        sum_of_row = 0
        for j in range(100):
            sum_of_col += arr[i][j]
            sum_of_row += arr[j][i]

        if sum_of_col > max_value:
            max_value = sum_of_col

        if sum_of_row > max_value:
            max_value = sum_of_row

    # 대각선 확인
    for i in range(100):
        sum_of_right_diagonal += arr[i][i]
        sum_of_left_diagonal += arr[99-i][i]

    if sum_of_right_diagonal > max_value:
        max_value = sum_of_right_diagonal
    if sum_of_left_diagonal > max_value:
        max_value = sum_of_left_diagonal

    print('#{} {}'.format(test_case, max_value))