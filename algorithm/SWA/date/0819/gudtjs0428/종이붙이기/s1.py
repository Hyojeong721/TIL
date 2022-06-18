import sys
sys.stdin = open('input.txt')

def how_many_ways(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        if N % 2:
            return 2 * how_many_ways(N-1) - 1
        else:
            return 3 * how_many_ways(N-2) + how_many_ways(N-2) - 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, how_many_ways(N // 10)))