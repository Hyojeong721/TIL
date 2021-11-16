import sys
sys.stdin = open('input.txt')



for T in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max = 0
    tmp = 0
    # 가로 비교
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            tmp += arr[row][col]
        if tmp > max:
            max = tmp
        tmp = 0
    # 세로 비교
    for col in range(len(arr)):
        for row in range(len(arr)):
            tmp += arr[row][col]
        if tmp > max:
            max = tmp
        tmp = 0

    # 우하향 대각선 비교
    row = 0
    col = 0
    while 0<= row < 100 and 0<= col < 100:
        tmp += arr[row][col]
        row += 1
        col += 1

    if tmp > max:
        max = tmp
    tmp = 0

    col = len(arr)
    row = 0
    # 좌하향 대각선 비교
    while 0 <= row < 100 and 0 <= col < 100:
        tmp += arr[row][col]
        row += 1
        col -= 1


    if tmp > max:
        max = tmp
    tmp = 0



    print('#{} {}'.format(tc, max))