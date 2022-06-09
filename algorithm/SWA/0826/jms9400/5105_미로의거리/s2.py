import sys

sys.stdin = open('input.txt')

T = int(input())


# 상하좌우로 돌며 길인 곳 찾아가기
def find_miro(n):
    global result
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    a, b = n
    for x in range(4):
        xi = a + dx[x]
        yi = b + dy[x]
        if xi in range(N) and yi in range(N):
            if miro[xi][yi] == 0 and visited[xi][yi] == 0:
                visited[xi][yi] = visited[a][b] + 1
                find_miro((xi, yi))
            elif miro[xi][yi] == 3:
                result = visited[a][b]
                return
    return


for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0

    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                n = (i, j)
                break

    find_miro(n)
    print('#{} {}'.format(tc, result))