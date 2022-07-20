import sys
sys.stdin = open('input.txt')

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
board = set()
board.add(arr[0][0])
ans = 0
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, cnt):
    global board, ans
    ans = max(ans, cnt)
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in board:
            board.add(arr[ni][nj])
            dfs(ni, nj, cnt+1)
            board.remove(arr[ni][nj])


dfs(0, 0, 1)


print(ans)