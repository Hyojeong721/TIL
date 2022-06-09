import sys
sys.stdin = open('input.txt')

def perm(n, k, cur_mul):
    global ans
    ###### 가지치기
    if ans >= cur_mul:
        return

    ######
    if n == k:
        if ans < cur_mul:
            ans = cur_mul
    else:
        for i in range(n):
            if u[i] == 0:
                u[i] = 1
                p[k] = i
                perm(n, k+1, cur_mul * (arr[k][p[k]]/100))
                u[i] = 0

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [0] * N
    u = [0] * N
    ans = 0
    perm(N, 0, 1)
    print('#%d %.6f' %(tc, ans * 100))

