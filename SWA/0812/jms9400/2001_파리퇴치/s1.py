import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(0, N-M+1):
        for j in range(N-M+1):
            total = 0
            # 가로세로줄 저장
            for k in range(M):
                for n in range(M):
                    total += arr[i+k][j+n]
            if total >= result:
                result = total
    print('#{} {}'.format(tc, result))