import sys
sys.stdin = open('input.txt')
def success(n, ans):
    global N, max_ans

    if ans < max_ans:
        return

    if n == N:
        max_ans = ans
        return


    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            new_ans = ans * rate[n][i] / 100
            success(n+1, new_ans)
            visited[i] = 0

T = int(input())
for tc in range(1):
    N = int(input())
    rate = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N)

    max_ans = 0

    success(0, 100)

    print("#{} {:6f}".format(tc, max_ans))