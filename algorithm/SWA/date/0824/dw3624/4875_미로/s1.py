# Fail (제한시간 초과)
import sys
sys.stdin = open('input.txt')

# 방향 : 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(y, x):
    global result

    if mat[y][x] == 3:
        result = 1
        return result

    visited.append([y, x])
    print(visited)

    # 상하좌우 칸 확인
    for d in range(4):
        new_y = y + dy[d]
        new_x = x + dx[d]

        if (mat[new_y][new_x] == 0 or mat[new_y][new_x] == 3) \
                and [new_y, new_x] not in visited:
            print([new_y, new_x])
            DFS(new_y, new_x)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    # padding 추가한 matrix 생성
    mat = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    mat = [[1] * (N + 2)] + mat + [[1] * (N + 2)]
    [print(m) for m in mat]

    # 시작점, 도착점 idx 탐색
    start, goal = [], []
    for row in range(N + 2):
        for col in range(N + 2):
            if mat[row][col] == 2:
                start.extend([row, col])

    result = 0
    visited = []
    DFS(start[0], start[1])
    print('#{} {}'.format(t, result))
