import sys
from itertools import permutations
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ability = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0
    for allocation in permutations(range(N), N):
        total = 1
        for i in range(N):
            total *= ability[i][allocation[i]]/100
            if total < maximum:
                break
        else:
            maximum = total

    print(maximum)



