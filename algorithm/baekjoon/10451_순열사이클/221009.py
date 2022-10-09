import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

def dfs(next):
    global visited, cnt

    idx = arr[0].index(next)
    num = arr[1][idx]
    # print('next', next, 'idx', idx, 'num', arr[1][idx])

    if next == num:
        return
    if not visited[num]:
        visited[num] = True
        dfs(num)




T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    arr = [[i for i in range(1, N+1)]]
    temp = list(map(int, input().split()))
    arr.append(temp)
    visited = [False for _ in range(N+1)]
    for i in range(N):
        next = arr[1][i]
        if not visited[next]:
            visited[next] = True
            dfs(next)
            cnt += 1

    print(cnt)