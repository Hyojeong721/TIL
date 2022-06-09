import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = []

    for _ in range(N):
        arr.append(list(map(int, input().split())))
    total = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                di = [0, 0, -1, 1]
                dj = [-1, 1, 0, 0]
                if i + di[k] in range(N) and j + dj[k] in range(N):
                    total += abs(arr[i][j] - arr[i + di[k]][j + dj[k]])

    print('#{0} {1}'.format(test_case, total))