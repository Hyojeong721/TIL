import sys
sys.stdin = open('input.txt')

T = int(input())


def find_miro(stack):


    while len(stack):
        i, j = stack.pop()
        visited[i][j] = 1
        if j+1 in range(N) and miro[i][j+1] == 3 or j-1 in range(N) and miro[i][j-1] == 3 \
                or i-1 in range(N) and miro[i-1][j] == 3 or i+1 in range(N) and miro[i+1][j] == 3:
            return 1

        if i-1 in range(N) and miro[i-1][j] == 0 and visited[i-1][j] == 0:
            stack.append((i-1, j))
        if j-1 in range(N) and miro[i][j-1] == 0 and visited[i][j-1] == 0:
            stack.append((i, j-1))
        if j+1 in range(N) and miro[i][j+1] == 0 and visited[i][j+1] == 0:
            stack.append((i, j+1))
        if i+1 in range(N) and miro[i+1][j] == 0 and visited[i+1][j] == 0:
            stack.append((i+1, j))
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
                break

    print('#{} {}'.format(tc, find_miro(stack)))