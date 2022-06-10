import sys
sys.stdin = open("input.txt")



T = 6
for tc in range(T):
    w, h = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False]*w for _ in range(h)]

    def is_range(x, y):
        if 0 <= x < h and 0 <= y < w:
            return True
        return False

    def bfs(x, y):
        # 좌, 우, 상, 하, 11시, 2시, 7시 5시
        di = [0, 0, -1, 1, -1, -1, 1, 1]
        dj = [-1, 1, 0, 0, -1, 1, -1, 1]
        temp = [(x, y)]
        while temp:
            i, j = temp.pop(0)
            for k in range(8):
                ni, nj = i+di[k], j+dj[k]
                if is_range(ni, nj):
                    if not visited[ni][nj] and arr[ni][nj]==1:
                        visited[ni][nj] = True
                        temp.append((ni, nj))




    cnt = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j]==1:
                bfs(i, j)
                cnt += 1

    print(cnt)
