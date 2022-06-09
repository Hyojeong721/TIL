import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    sequence = list(map(int, input().split()))
    print('#{} {}'.format(tc, sequence[M % N]))