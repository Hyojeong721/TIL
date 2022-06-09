import sys
sys.stdin = open('input.txt')

def find(k, cursum):
    global ans
    if cursum > ans:
        return

    if k == N:
        if cursum < ans:
            ans = cursum
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                find(k+1, cursum + V[k][i])
                visited[i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * N
    visited = [0] * N
    # print(V)
    find(0, 0)
    print('#{} {}'.format(tc, ans))