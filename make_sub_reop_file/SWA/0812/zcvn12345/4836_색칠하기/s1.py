import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for i in range(10)]
    for paint in range(N):
        color = list(map(int, input().split()))
        for x in range(color[1], color[3]+1):
            for y in range(color[0], color[2]+1):
                arr[y][x] += 1

    count = 0
    for i in arr:
        for j in i:
            if j == 2:
                count += 1

    print('#{0} {1}'.format(test_case, count))
