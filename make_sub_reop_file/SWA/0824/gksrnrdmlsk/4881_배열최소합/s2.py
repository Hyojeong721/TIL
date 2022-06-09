# 양심 없는 풀이
from itertools import permutations
import sys
sys.stdin = open('input.txt')

p10 = list(permutations(range(10), 10))
p9 = list(permutations(range(9), 9))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    if N < 9:
        p = list(permutations(range(N), N))
        result = min([sum([lst[i][j[i]] for i in range(N)]) for j in p])
        print('#{} {}'.format(tc, result))

    elif N == 9:
        result = min([sum([lst[i][j[i]] for i in range(N)]) for j in p9])
        print('#{} {}'.format(tc, result))

    else:
        result = min([sum([lst[i][j[i]] for i in range(N)]) for j in p10])
        print('#{} {}'.format(tc, result))