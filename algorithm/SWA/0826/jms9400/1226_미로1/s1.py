import sys
sys.stdin = open('input.txt')

T = 10


def find_miro(s):

    global result
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while stack:
        a, b = stack.pop(0)
        for x in range(4):
            xi = a + dx[x]
            yi = b + dy[x]
            if miro[xi][yi] == 0 and visited[xi][yi] == 0:
                stack.append((xi, yi))
                visited[xi][yi] = 1
            elif miro[xi][yi] == 3:
                result = 1
                return
    return


for tc in range(1, T + 1):
    N = 16
    n = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    stack = []

    for i in range(1, N-1):
        for j in range(1, N-1):
            if miro[i][j] == 2:
                stack.append((i, j))
                break

    find_miro(stack)
    print('#{} {}'.format(tc, result))