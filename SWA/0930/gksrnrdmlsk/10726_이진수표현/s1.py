import sys
sys.stdin = open('input.txt')

def determine(N, M):
    number = bin(M)[2:]
    length = len(number)
    if length < N:
        return 'OFF'
    else:
        for i in number[-N:]:
            if i == '0':
                return 'OFF'
    return 'ON'

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, determine(N, M)))