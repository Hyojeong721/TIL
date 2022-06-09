import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T+1):
    N = float(input())
    result = ''
    for i in range(1, 13):
        m = 2**(-i)
        if N >= m:
            N -= m
            result += '1'
        else:
            result += '0'

        if N == 0:
            break
    if N > 0:
        result = 'overflow'

    print('#{} {}'.format(tc, result))