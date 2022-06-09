import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# def search(r, c, cur, cuc, cnt):
#     global answer
#     if answer < cnt:
#         answer = cnt
#         winner = (r, c)
#
#     for i in range(4):
#         nr = cur + dx[i]
#         nc = cuc+ dy[i]
#         if 0 <= nr < N and 0 <= nc <N and lst[nr][nc] == lst[cur][cuc] + 1:
#             search(r, c, nr, nc, cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    dq = deque([])
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if lst[nr][nc] == lst[r][c] - 1:
                        dq = deque([])
                        break
                    elif lst[nr][nc] == lst[r][c] + 1:
                        dq.append([nr, nc, 2])
            if dq:
                while dq:
                    x, y, cnt = dq.popleft()
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == lst[x][y] + 1:
                            dq.append([nx, ny, cnt + 1])
                if answer < cnt:
                    answer = cnt
                    numbers = [lst[r][c]]
                elif answer == cnt:
                    numbers.append(lst[r][c])

    print('#{} {} {}'.format(tc, min(numbers), answer))
