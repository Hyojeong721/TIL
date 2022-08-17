import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
res = []
def dfs(res):
    if len(res) == M:
        print(*res)
        return

    for i in arr:
        if i not in res:
            res.append(i)
            dfs(res)
            res.pop()

dfs([])