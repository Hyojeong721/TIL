import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
res = -1
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

