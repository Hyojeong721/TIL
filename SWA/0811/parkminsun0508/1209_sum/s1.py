# 1209_SUM
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하라
import sys
sys.stdin = open('input.txt')

TC = 10
for tc in range(1, TC+1):
    x = int(input())
    numb_list = []
    for num in range(100):
        numbers = list(map(int, input().split()))
        num_list.append(numbers)

    max_number = 0
    for i in range(100):
        row_sum = 0
        column_sum = 0
        for j in range(100):
            row_sum += num_list[i][j]
            column_sum += num_list[j][i]
        if max_number < row_sum:
            max_number = row_sum
        if max_number < column_sum:
            max_number = column_sum

    cross_sum = 0
    cross_sum2 = 0
    for i in range(100):
        cross_sum += num_list[i][i]
        cross_sum2 += num_list[i][99 - i]
    if max_number < cross_sum:
        max_number = cross_sum
    if max_number < cross_sum2:
        max_number = cross_sum2

    print("#%d" %tc, max_number)