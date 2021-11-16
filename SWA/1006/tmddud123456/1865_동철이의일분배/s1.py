import sys
sys.stdin = open('input.txt')

def max_percent(i, temp):
    global mat, check, total
    if temp <= total:
        return
    if i == N:
        if total < temp:
            total = temp
            return

    for j in range(N):
        if check[j] == 0 and total < temp*(mat[i][j]/100):
            check[j] = 1
            max_percent(i+1, temp*(mat[i][j]/100))
            check[j] = 0


TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    check = [0]*N
    total = 0
    max_percent(0, 100)
    print('#{} {:.6f}'.format(tc, total))
