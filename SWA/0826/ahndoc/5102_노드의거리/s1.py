import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for g in graph_list:
        graph[g[0]][g[1]] = 1
        graph[g[1]][g[0]] = 1

    q = []
    q.append(S)
    visited = [0] * (V+1)
    visited[S] = 1
    while q:
        t = q.pop(0)

        for i in range(1, V+1):
            if graph[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t] + 1

    if visited[G]:
        result = visited[G] - 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))





