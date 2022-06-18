import sys
sys.stdin = open('input.txt')

T = int(input())

dy = [0, 1]   # 우하좌상
dx = [1, 0]

def search(x, y, total):
    global mat, N, min_total
    total += mat[y][x]
    if total > min_total:
        return
    if x == N-1 and y == N-1:
        if total < min_total:
            min_total = total


    else:
        for i in range(2):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < N and 0 <= ty < N:
                search(tx, ty, total)

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_total = 100000000000
    search(0, 0, 0)
    print(f'#{tc} {min_total}')