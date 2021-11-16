# 패키지 사용으로 runtime error 발생
import sys
from itertools import permutations as perm
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    arr = [x for x in range(N)]

    result = 9*N
    for combination in list(perm(arr, N)):
        total = 0
        for i in range(N):
            total += matrix[i][combination[i]]
            if total >= result:
                break
        if total < result:
            result = total

    print(f'#{tc} {result}')








