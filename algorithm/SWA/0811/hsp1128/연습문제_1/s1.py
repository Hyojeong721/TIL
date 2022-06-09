import sys
sys.stdin = open('input.txt')

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
        N = int(input())
        arr = [list(map(int, input().split())) for _ in range(N)]
        result = 0
        for i in range(len(arr)):
                for j in range(len(arr[i])):
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if 0 <= ni < N and 0 <= nj < N:
                                result += abs(arr[ni][nj] - arr[i][j])


        print(result)







