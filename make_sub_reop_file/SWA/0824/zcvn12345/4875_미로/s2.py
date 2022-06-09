import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    V = N * N
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
