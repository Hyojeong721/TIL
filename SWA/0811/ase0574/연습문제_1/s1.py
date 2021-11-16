import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[int(x) for x in input().split()] for y in range(N)]
    result = 0

    for r in range(N):
        for c in range(N):

            if r-1 >= 0 and arr[r-1][c]:
                top = abs(arr[r][c] - arr[r-1][c])
            else:
                top = 0

            if r+1 < N and arr[r+1][c]:
                bottom = abs(arr[r][c] - arr[r+1][c])
            else:
                bottom = 0

            if c-1 >= 0 and arr[r][c-1]:
                left = abs(arr[r][c] - arr[r][c-1])
            else:
                left = 0

            if c+1 < N and arr[r][c+1]:
                right = abs(arr[r][c] - arr[r][c+1])
            else:
                right = 0

            #모든 차이의 절댓값을 result에 더함!

            result += top + bottom + left + right

    print('#{} {}'.format(tc, result))

