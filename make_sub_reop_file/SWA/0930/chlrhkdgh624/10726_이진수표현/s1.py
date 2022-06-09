import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


def check(a, b):
    result = ''
    for i in range(a):
        if b & (1 << i):
            result += '1'
        else:
            result += '0'
    status = 'ON'
    if '0' in result:
        status = 'OFF'
    return status


for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = check(N, M)
    print('#{} {}'.format(tc, ans))