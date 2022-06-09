import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    number = M & (2 ** N - 1)
    if number ^ (2 ** N - 1):
        print('#{} {}'.format(tc, 'OFF'))
    else:
        print('#{} {}'.format(tc, 'ON'))

