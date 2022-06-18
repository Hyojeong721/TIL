import sys
sys.stdin = open('input.txt')

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def DFS(y, x):
    global result

    if mat[y][x] == 3:
        result = 1
        return True

    stack.append((y, x))

    # 갈 수 있는 경로 탐색
    for d in range(4):
        new_y = y + dy[d]
        new_x = x + dx[d]

        # 갈 수 있는 경로
        if 0 <= new_y < N and 0 <= new_x < N:
            if mat[new_y][new_x] != 1 and (new_y, new_x) not in stack:
                DFS(new_y, new_x)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    # [print(m) for m in mat]

    start = []
    for row in range(N):
        for col in range(N):
            if mat[row][col] == 2:
                start.extend([row, col])
    result = 0
    stack = []
    DFS(start[0],start[1])
    print('#{} {}'.format(t, result))