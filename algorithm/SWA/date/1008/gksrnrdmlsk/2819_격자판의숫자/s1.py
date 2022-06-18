import sys
sys.stdin = open('input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search(r, c, num):
    if len(num) == 7:
        results.add(''.join(num))
    else:
        for i in range(N):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                search(nr, nc, num + [lst[nr][nc]])

T = int(input())
for tc in range(1, T + 1):
    N = 4
    lst = [list(input().split()) for _ in range(N)]
    results = set()
    for i in range(N):
        for j in range(N):
            search(i, j, [lst[i][j]])
    print('#{} {}'.format(tc, len(results)))