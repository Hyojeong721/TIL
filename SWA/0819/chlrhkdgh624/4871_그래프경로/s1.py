import sys
sys.stdin = open('input.txt')

T = int(input())


def dfs(start, end):
    global visited
    visited[start] = 1
    stack = []
    i = start

    while i != 0:
        for w in range(1, V+1):
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = 0

    if visited[end] == 1:
        return 1
    else:
        return 0


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        x, y = list(map(int, input().split()))
        graph[x][y] = 1

    visited = [0] * (V + 1)

    S, G = list(map(int, input().split()))
    result = dfs(S, G)

    print(f'#{tc} {result}')







