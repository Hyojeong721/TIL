import sys
sys.stdin = open('input.txt')

def bfs(s, g):
    queue = [s]

    while len(queue):
        s = queue.pop(0)

        for w in range(1, V+1):
            if edge[s][w] == 1 and dist[w] == 0:
                queue.append(w)
                dist[w] = dist[s] + 1

    return dist[g]

T = int(input())

for test_case in range(1, T+1):
    V, E = list(map(int, input().split()))
    edge = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        v1, v2 = map(int, input().split())
        edge[v1][v2] = 1
        edge[v2][v1] = 1
    S, G = list(map(int, input().split()))
    dist = [0 for _ in range(V + 1)]

    print('#{} {}'.format(test_case, bfs(S, G)))