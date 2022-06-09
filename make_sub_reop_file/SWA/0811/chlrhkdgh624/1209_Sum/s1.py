import sys
sys.stdin = open('input.txt')

T = 10

for t in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []
    # 각 행의 합
    for row in range(100):
        row_sum = 0
        for num in arr[row]:
            row_sum += num
        result.append(row_sum)

    # 각 열의 합
    for col in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][col]
        result.append(col_sum)

    # 두 대각선의 합
    from_left = 0
    from_right = 0
    for col in range(100):
        for row in range(100):
            if col == row:
                from_left += arr[row][col]
            elif col + row == 99:
                from_right += arr[row][col]

    result.extend([from_left, from_right])

    # result 정렬
    for i in range(len(result), 0, -1):
        for j in range(0, i-1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    print(f'#{tc} {result[-1]}')





