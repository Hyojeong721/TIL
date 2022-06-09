import sys
sys.stdin = open('sample_input.txt')
T = int(input())


def bfs(start, end):
    global adj, V
    q_idx = [0] * (V+1)
    queue = [start]

    while len(queue):
        i = queue.pop(0)
        cnt = q_idx[i]
        for j in range(1, V+1):
            if adj[i][j] == 1 and q_idx[j] == 0:
                queue.append(j)
                q_idx[j] = cnt+1
        if end in queue:
            return q_idx[end]
    else:
        return 0


for tc in range(1, T+1):
    V, E = list(map(int, input().split()))  # V = 노드 개수, E = 간선 개수
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y = list(map(int, input().split()))
        adj[x][y] = 1
        adj[y][x] = 1

    S, G = list(map(int, input().split()))
    result = bfs(S, G)

    print(f'#{tc} {result}')




