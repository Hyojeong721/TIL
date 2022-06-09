import sys
sys.stdin = open('input.txt')


def dfs():
    global visited, stack
    visited[0] = 1
    i = 0

    while i != -1:
        for w in range(100):
            if graph[i][w] == 1 and visited[w] == 0:
                stack.append(i)
                i = w
                visited[w] = 1
                break
        else:
            if stack:
                i = stack.pop()
            else:
                i = -1

    if visited[-1] == 1:
        return 1
    else:
        return 0


T = 10

for _ in range(1, T+1):
    tc, E = list(map(int, input().split()))
    graph = [[0]*100 for _ in range(100)]
    connect = list(map(int, input().split()))

    for _ in range(E):
        x = connect.pop(0)
        y = connect.pop(0)
        graph[x][y] = 1

    visited = [0]*100
    stack = []

    print(f'#{tc} {dfs()}')


