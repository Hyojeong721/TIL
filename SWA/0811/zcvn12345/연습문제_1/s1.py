import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    total = 0
    for x in range(N):
        for y in range(N):
            for i in range(4):
                test_x = x + dx[i]
                test_y = y + dy[i]
                if 0 <= test_x <= 4 and 0 <= test_y <= 4:
                    total += abs(arr[x][y] - arr[test_x][test_y])
    print('#{0} {1}'.format(test_case, total))




