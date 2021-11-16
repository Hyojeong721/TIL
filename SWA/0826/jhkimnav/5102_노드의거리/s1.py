import sys
sys.stdin = open('input.txt')


def dfs(S, G, V):
    q = []
    visited = [0] * (V + 1)
    q.append(S)
    visited[S] = 1

    while q:
        v = q.pop(0)
        if v == G:
            return visited[v] - 1
        for i in range(1, V+1):
            if graph[v][i] and not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    return 0


T = int(input())
for TC in range(1, T+1):
    answer = 0
    # V : 노드 개수
    # E : 간선 개수
    V, E = list(map(int, input().split()))
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end = list(map(int, input().split()))
        graph[start][end] = 1
        graph[end][start] = 1

    # 출발노드, 도착노드
    S, G = list(map(int, input().split()))
    answer = dfs(S, G, V)
    print('#{} {}'.format(TC, answer))