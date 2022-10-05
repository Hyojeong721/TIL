import sys
from collections import deque

T = int(sys.stdin.readline())

def is_range(i, j):
    if 0 <= i < H and 0 <= j < W:
        return True
    return False

def bfs():
    di, dj= [-1, 1, 0, 0], [0, 0, -1, 1]
    while person:
        # 불 번짐
        for _ in range(len(fires)):
            x, y = fires.popleft()
            for k in range(4):
                ni, nj = x+di[k], y+dj[k]
                if is_range(ni, nj) and arr[ni][nj] in ('.', '@'):
                    arr[ni][nj] = '*'
                    fires.append((ni, nj))
        # 사람 이동
        for _ in range(len(person)):
            i, j, cnt = person.popleft()
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if is_range(ni, nj):
                    if arr[ni][nj] not in ('#', '*', '@'):
                        person.append((ni, nj, cnt+1))
                        arr[ni][nj] = '@'
                else:
                    return cnt+1
    return -1


for tc in range(T):
    person = deque()
    fires = deque()
    arr = []
    W, H = map(int, sys.stdin.readline().split())

    for h in range(H):
        temp = list(sys.stdin.readline().strip())
        arr.append(temp)
        for w in range(W):
            if temp[w] == '@':
                person.append((h, w, 0))
                # arr[h][w] = '.'
            if temp[w] == '*':
                fires.append((h, w))

    res = bfs()
    if res == -1:
        print('IMPOSSIBLE')
    else:
        print(res)