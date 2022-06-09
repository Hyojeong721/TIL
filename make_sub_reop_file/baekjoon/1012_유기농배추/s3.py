# 2022.03.17
import collections
import sys
sys.stdin = open("input.txt")

def bfs(back, x, y,m,n):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = collections.deque()
    q.append((x, y))

    while q:
        now = q.popleft()

        back[now[1]][now[0]] = 0

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if back[ny][nx] == 1:
                back[ny][nx] = 0
                q.append((nx, ny))
    return

T = int(input())
for tc in range(1, T+1):
    m,n,k = map(int, input().split())
    back = [[0 for _ in range(m)] for i in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        back[y][x] = 1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if back[y][x] == 1:
                bfs(back, x, y, m ,n)
                cnt += 1
    print(cnt)