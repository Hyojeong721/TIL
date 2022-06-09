# 0824 _ runtime error
import sys
sys.stdin = open('input.txt')

T = int (input())

for tc in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    result = [0] * (P+1)

    for i in bus:
        for j in range(i[0],i[1]+1):
            result[j] += 1
    print('#{}'.format(tc), end=' ')
    print(*result[1:])


