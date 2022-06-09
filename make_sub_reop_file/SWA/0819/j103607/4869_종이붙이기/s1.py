import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    # 직사각형 크기: 20*N
    N = int(input())
    n = N//10

    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 3

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]*2

    print('#{} {}'.format(tc, memo[-1]))