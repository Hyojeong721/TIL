import sys
sys.stdin = open('input.txt')

T = int(input())


def find_miro(i, j):

    dx = [-1, 0, 1, 0]  # 상우하좌
    dy = [0, 1, 0, -1]
    global result

    for x in range(4):
        if i + dx[x] in range(N) and j + dy[x] in range(N):
            if miro[i+dx[x]][j+dy[x]] == 3:
                result = 1
                return
            if miro[i+dx[x]][j+dy[x]] == 0:
                miro[i+dx[x]][j+dy[x]] = 5
                find_miro(i+dx[x], j+dy[x])

for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 출발지점 저장
    for n in range(N):
        for m in range(N):
            if miro[n][m] == 2:
                break
    result = 0
    find_miro(n, m)
    print(result)

