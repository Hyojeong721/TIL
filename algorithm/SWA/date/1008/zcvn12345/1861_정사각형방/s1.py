import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def search(cnt, x, y):
    global mat, N
    for w in range(4):
        tx = x + dx[w]
        ty = y + dy[w]
        if 0 <= tx < N and 0 <= ty < N:
            if mat[y][x] != (mat[ty][tx]+1):
                cnt_lst.append((mat[y][x], cnt))
                continue
            elif mat[y][x] == (mat[ty][tx]+1):
                search(cnt+1, tx, ty)
    return


for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    cnt_lst = []
    for i in range(N):
        for j in range(N):
            search(1, i, j)

