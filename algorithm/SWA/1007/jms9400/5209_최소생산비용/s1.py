import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(a, total):
    global answer

    if total >= answer:
        return

    if a == N:
        if total <= answer:
            answer = total
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(a+1, total+arr[a][i])
            visited[i] = 0

# visited배열 쓰지 않고 정수 활용
def dfs2(a, total, visit):
    global answer

    if total >= answer:
        return

    if a == N:
        if total < answer:
            answer = total
        return

    for j in range(N):
        if visit & (1 << j): continue
        dfs2(a+1, total + arr[a][j], visit | (1 << j))


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 0

    for i in range(N):
        answer += arr[i][i]

    dfs(0, 0)

    print('#{} {}'.format(tc, answer))