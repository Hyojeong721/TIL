import sys
sys.stdin = open('sample_input.txt')
T = int(input())


def my_bfs(s, V):
    visited = [0] * (V+1)
    queue = [s]
    visited[s] = 0

    while len(queue):
        s = queue.pop(0)
        for w in range(1, V+1):
            if adj[s][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[s]+1
    return visited


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))  # V = 노드 개수, E = 간선 개수
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = list(map(int, input().split()))
        adj[x][y] = 1
        adj[y][x] = 1

    S, G = list(map(int, input().split()))
    result = my_bfs(S, V)

    print(f'#{tc} {result[G]}')
