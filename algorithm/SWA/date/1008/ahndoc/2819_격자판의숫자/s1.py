import sys
sys.stdin = open('input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def find(r, c, num):

    if len(num) == 7:
        if num in visited:
            return
        visited.add(num)
        return
    else:
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                find(nr, nc, num + numbers[nr][nc])


T = int(input())
for tc in range(1, T+1):
    numbers = [input().split() for _ in range(4)]
    visited = set()

    for i in range(4):
        for j in range(4):
            find(i, j, numbers[i][j])
    print('#{} {}'.format(tc, len(visited)))