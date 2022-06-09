import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for i in range(N)]
    # 채워지는 숫자
    num = 1
    # 방향 전환 후 숫자가 채워지는 횟수
    r = int(N)
    # 숫자가 채워지는 좌표
    x = -1
    y = 0
    while r > 0:
        # 오른쪽
        for right in range(r):
            x += 1
            arr[y][x] = num
            num += 1
        r -= 1
        # 아래로
        for down in range(r):
            y += 1
            arr[y][x] = num
            num += 1
        # 왼쪽
        for left in range(r):
            x -= 1
            arr[y][x] = num
            num += 1
        r -= 1
        # 위로
        for up in range(r):
            y -= 1
            arr[y][x] = num
            num += 1

    print('#{}'.format(test_case))
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()


