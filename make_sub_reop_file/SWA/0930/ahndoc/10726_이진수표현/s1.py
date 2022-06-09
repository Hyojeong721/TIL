import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 'OFF'
    M = str(format(M, 'b'))

    if len(M) >= N:
        if '0' in M[len(M)-N:len(M)]:
            pass
        else:
            result = 'ON'
    else:
        while len(M) != N:
            M = '0' + M
        if '0' in M[len(M)-N:len(M)]:
            pass
        else:
            result = 'ON'

    print('#{} {}'.format(tc, result))
