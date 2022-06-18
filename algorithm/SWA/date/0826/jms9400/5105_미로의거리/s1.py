import sys
sys.stdin = open('input.txt')

T = int(input())

# 상하좌우로 돌며 길인 곳 찾아가기
def find_miro(stack):
    global result
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while stack:
        a, b = stack.pop(0)
        for x in range(4):
            if a+dx[x] in range(N) and b+dy[x] in range(N):
                if miro[a+dx[x]][b+dy[x]] == 0 and visited[a+dx[x]][b+dy[x]] == 0:
                    stack.append((a+dx[x], b+dy[x]))
                    visited[a+dx[x]][b+dy[x]] = visited[a][b] + 1
                elif miro[a+dx[x]][b+dy[x]] == 3:
                    result = visited[a][b]
                    return


for tc in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 0
    stack = []

    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                stack.append((i, j))
                break

    find_miro(stack)
    print('#{} {}'.format(tc, result))