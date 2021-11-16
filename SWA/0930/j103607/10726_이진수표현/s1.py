import sys
sys.stdin = open('input.txt')


TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())



    T = int(input())
    for tc in range(T):
        N, M = map(int, input().split())
        for i in range(N):
            if not M % 2:
                res = 'OFF'
            M //= 2
        else:
            res = 'ON'

        print('#{} {}'.format(tc + 1, res))