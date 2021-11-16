import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    paskal = [[1 for _ in range(i)] for i in range(1, N+1)]

    for i in range(2, N):
        for j in range(1, i):
            paskal[i][j] = paskal[i-1][j-1] + paskal[i-1][j]

    print('#{}'.format(tc))
    for i in paskal:
        print(*i)



