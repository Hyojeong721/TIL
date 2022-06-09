import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 'ON'
    for i in range(N):
        if not M % 2:
            result = 'OFF'
        M //= 2
    print(f'#{tc} {result}')