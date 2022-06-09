import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for x in range(M):
                for y in range(M):
                    tmp += arr[i+x][j+y]
            if tmp > max:
                max = tmp




    print('#{} {}'.format(tc, max))







