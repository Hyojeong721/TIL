import sys
sys.stdin = open('input.txt')

def find_min


T = int(input())
for tc in range(1, T+1):
    # 배열의 길이
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    partial_sum = 0
    min_sum = 1000
    find_min(0)