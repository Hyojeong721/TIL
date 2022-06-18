import sys
sys.stdin = open('input.txt')

def is_road(s, g):
    global graph,V
    visited = [0 for _ in range(V + 1)]
    stack = [s]
    while stack:
        current = stack.pop()
        if visited[current] == 0:
            visited[current] = 1
            for i in range(1, V + 1):
                if graph[current][i] == 1 and visited[i] == 0:
                    stack.append(i)

    if visited[g] == 1:
        return 1

    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        r, c = map(int, input().split())
        graph[r][c] = 1

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, is_road(S, G)))