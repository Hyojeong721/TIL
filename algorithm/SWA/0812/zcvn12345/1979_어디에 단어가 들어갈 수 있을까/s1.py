import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
