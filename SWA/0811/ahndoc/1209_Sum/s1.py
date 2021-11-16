import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    total_list = []

    # 행의 합
    for i in range(100):
        row_total = 0
        for j in range(100):
            row_total += arr[i][j]
        total_list.append(row_total)
    # 열의 합
    for j in range(100):
        col_total = 0
        for i in range(100):
            col_total += arr[i][j]
        total_list.append(col_total)

    # 대각선의 합
    crossR_total = 0
    for i in range(100):
        crossR_total += arr[i][i]
    total_list.append(crossR_total)

    crossL_total = 0
    for i in range(100):
        crossL_total += arr[99-i][i]
    total_list.append(crossL_total)

    # 최대값 도출
    max_v = total_list[0]
    for v in total_list:
        if v > max_v:
            max_v = v

    print('#{} {}'.format(test_case, max_v))


    # 100 X 100 에서 모든 대각선을 합할 경우
    # for i in range(100):
    #     crossR = 0
    #     crossL = 0
    #     for j in range(100):
    #         for k in range(99):
    #             if j-i == k:
    #                 crossR += arr[i][j]
    #             if i-j == k:
    #                 crossL += arr[i][j]
    #
    #     print(crossR, end= ' ')
    #     print(crossL, end= ' ')
    # print()









