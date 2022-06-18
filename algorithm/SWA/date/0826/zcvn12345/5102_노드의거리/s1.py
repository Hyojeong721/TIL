import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1)for _ in range(V+1)]
    for i in range(E):
        e = list(map(int, input().split()))
        graph[e[0]][e[1]] = 1
        graph[e[1]][e[0]] = 1
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    q = []
    q.append(S)
    visited[S] = 1
    while q:
        t = q.pop(0)
        for i in range(1, V+1):
            if graph[t][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1
    if visited[G] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {visited[G]-1}')
