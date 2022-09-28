import sys
sys.stdin = open('input.txt')
from collections import deque


def is_range(i , j):
    if 0<=i<R and 0<=j<C and arr[i][j] != '#':
        return True
    return False

# 글자 '.' : 빈 필드/ '#': 울타리 /'o':양 / 'v': 늑대
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

visited = [[False]*C for _ in range(R)]
res_fox, res_sheep = 0, 0
que = deque()
# 구역 확인 + 양과 늑대 수 함께 확인
for i in range(R):
    for j in range(C):
        fox, sheep = 0, 0
        if not visited[i][j] and arr[i][j] != '#':
            que.append((i, j))
            while que:
                x, y = que.popleft()
                visited[x][y] = True
                if arr[x][y] == 'v':
                    fox += 1
                elif arr[x][y] == 'o':
                    sheep += 1

                for k in range(4):
                    ni, nj = x+di[k], y+dj[k]
                    if is_range(ni, nj) and not visited[ni][nj] and arr[ni][nj] != '#':
                        if not (ni, nj) in que:
                            que.append((ni, nj))

            # 양과 늑대 수 비교 후 최종 양, 최종 늑대 수에 반영
            if fox < sheep:
                res_sheep += sheep
            else:
                res_fox += fox

print(res_sheep, res_fox)