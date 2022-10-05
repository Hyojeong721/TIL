import sys
# sys.stdin = open('input.txt')
from collections import deque
### 이거 안됌
T = int(sys.stdin.readline())

def is_range(i, j):
    if 0<=i<H and 0<=j<w:
        return True
    return False


def bfs():
    while True:
        # print(que)
        #fire
        for _ in range(len(fires)):
            i, j = fires.popleft()
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if is_range(ni, nj) and (arr[ni][nj] == '.'or arr[ni][nj] == '@'):
                    arr[ni][nj] = '*'
                    fires.append((ni, nj))
        #person
        for _ in range(len(que)):
            # print(que)
            i, j = que.popleft()
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if is_range(ni, nj) and arr[ni][nj] == '.':

                    if ni == 0 or nj == 0 or ni == H-1 or nj == w-1:
                        return visited[i][j]
                    if visited[ni][nj] == 99999:
                        que.append((ni, nj))
                        visited[ni][nj] = visited[i][j] + 1
        if len(que) == 0:
            break
    return -1

for tc in range(T):
    w, H = map(int, sys.stdin.readline().split())
    # 지도
    arr = []
    # 불 위치 저장
    fires = deque()
    # 사람 위치
    que = deque()
    # 시간
    visited = [[99999] * w for _ in range(H)]
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 시작점
    for h in range(H):
        temp = list(sys.stdin.readline())
        arr.append(temp)

        if '@' in temp:
            idx = temp.index('@')
            start = (h, idx)
            que.append(start)
            visited[start[0]][start[1]] = 1

    # 시작점 없는 경우
    if not que:
        print('IMPOSSIBLE')
        continue

    # 불 입력
    for i in range(H):
        for j in range(w):
            if arr[i][j] == '*':
                fires.append((i, j))



    res = bfs()
    if res != -1:
        print(res)
    else:
        print('IMPOSSIBLE')
    #     res = 999999
    #     if min(visited[0]) == 1 or min(visited[-1]) == 1:
    #         res = 2
    #     else:
    #         # 첫행
    #         res = min(res, min(visited[0]))
    #         # 마지막행
    #         res = min(res, min(visited[-1]))
    #
    #     # 첫 열 / 마지막 열
    #     for h in range(H):
    #         if visited[h][0] == 1 or visited[h][-1] == 1:
    #             res = 1
    #             break
    #         res = min(res, visited[h][0])
    #         res = min(res, visited[h][-1])
    # print(res)