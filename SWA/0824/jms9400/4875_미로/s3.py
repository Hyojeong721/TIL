import sys
sys.stdin = open('input.txt')

T = int(input())


def find_miro(stack):

    dx = [-1, 0, 1, 0]  # 상우하좌
    dy = [0, 1, 0, -1]

    while len(stack):
        i, j = stack.pop()
        visited[i][j] = 1
        for x in range(4):
            i = i + dx[x]
            j = j + dy[x]
            if i in range(N) and j in range(N):
                if miro[i][j] == 3:
                    return 1
                elif miro[i][j] == 0 and visited:
                    stack.append((i+dx[x], j+dy[x]))
    return 0

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack = []

    # 출발지점 저장
    for n in range(N):
        for m in range(N):
            if miro[n][m] == 2:
                stack.append((n, m))

    find_miro(stack)