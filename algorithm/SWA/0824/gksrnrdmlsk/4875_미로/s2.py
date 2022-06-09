# 재귀 개점휴업

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [[1] * (N + 2)] + [[1] + list(map(int, list(input()))) + [1] for _ in range(N)] + [[1] * (N + 2)]
    print(lst)