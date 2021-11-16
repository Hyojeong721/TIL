import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1

    S, G = map(int, input().split())

    stack = [S]

    while stack:
        v = stack.pop()
        if visited[v] == 0:
            visited[v] = 1
        for w in range(1, V+1):
            if adj[v][w] == 1 and visited[w] == 0:
                stack.append(w)

    if visited[G]:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))