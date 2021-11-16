import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in (1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr[i][j] = j

        for