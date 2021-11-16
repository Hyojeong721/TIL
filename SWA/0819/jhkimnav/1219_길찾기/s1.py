# 인접 리스트
import sys
sys.stdin = open('input.txt')

def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == 99:
            return 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    return 0

for _ in range(10):
    answer = 0
    TC, E = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    edge_list = list(map(int, input().split()))
    visited = [0] * 100

    for i in range(E):
        start = edge_list[i*2]
        end = edge_list[i*2+1]
        graph[start].append(end)

    # 정점 V

    answer = bfs(0)
    print('#{} {}'.format(TC, answer))